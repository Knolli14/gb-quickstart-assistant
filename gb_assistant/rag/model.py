from transformers import pipeline
from sentence_transformers import SentenceTransformer
from gb_assistant.rag.chroma import setup_database
from gb_assistant.rag.bucket import download_blob
from gb_assistant.params import STORE_PATH, GC_BUCKET_NAME
import json

def load_model():
    """Instanciate the text generation model"""

    pipe = pipeline("text2text-generation", model="google/flan-t5-small")
    return pipe


def embed_query(query):
    """ Creates an embedded query using sentence-transformer """

    embed_model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
    return embed_model.encode(query)


def create_answer(model, query, gametitle):
    """
    Loads game specific embeddings, retrieves most relevant chunks
    and passes it to model for answer generation

    Returns:
    dict: Keys are answer and distance
    """

    # load game specific embeddings and metadata from Cloud Storage
    game_chunks = json.loads(download_blob(GC_BUCKET_NAME, "jsons/"+gametitle+".json"))

    # setting up vectorindex
    vindex = setup_database(STORE_PATH, "_".join(gametitle.split()), game_chunks) #names must have no whitespaces!!!

    # create an embedding of the query
    embedded_query = embed_query(query)

    # retrieving most relevant chunks
    query_results = vindex.query(query_embeddings=embedded_query,n_results=10)

    # extracting text corpus to create prompt
    context = " ".join(query_results["documents"][0])
    prompt = context + " " + query

    # receive answer by prompting llm
    response = model(prompt, max_length=100)

    return {"answer":response,
            "distance": query_results["distances"][0]}
