from transformers import pipeline
from sentence_transformers import SentenceTransformer
from gb_assistant.simple_model.chroma import setup_database
from gb_assistant.simple_model.bucket import download_blob
from gb_assistant.params import STORE_PATH, GC_BUCKET_NAME
import json
import os

def load_model():
    """Instanciate the text generation model"""
    qa_pipeline = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")
    return qa_pipeline



def create_answer(model, query, gametitle):

    store_path = STORE_PATH
    bucket_name = os.environ.get("GC_BUCKET_NAME")

    game_chunks = json.loads(download_blob("llama-index-knolli14", "jsons/"+gametitle+".json"))

    vindex = setup_database(store_path, gametitle, game_chunks)

    embed_model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
    embedded_query = embed_model.encode(query)

    query_results = vindex.query(query_embeddings=embedded_query,n_results=3)

    context = "\n\n".join(query_results["documents"][0])
    prompt = context+" "+query
    response = model(prompt, max_length=100)

    return response


# def answer_question(model, question:str):
#     """Answer the question passed as input"""
#     vector_store_path = "/Users/kirillkorzh/code/Knolli14/gb-quickstart-assistant/vector_store"  # Update this path to your PDF directory
#     client = chromadb.PersistentClient(vector_store_path)
#     collection = client.get_collection(
#         name="gb-assistant-complete"
#         )

#     # Load the LLM
#     qa_pipe = model

#     # Test the LLM with a sample query
#     query = "What are the rules for scoring in this game?"
#     embed_model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
#     embedded_query = embed_model.encode(query)
#     query_results = collection.query(query_embeddings=embedded_query,n_results=3)

#     context = "\n\n".join(query_results["documents"][0])
#     prompt = context+" "+query
#     response = qa_pipe(prompt, max_length=100)

#     return response

# new by Olli


#print(answer_question(load_model(),"how to win?"))
