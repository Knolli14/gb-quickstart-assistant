from transformers import pipeline
import gb_assistant.params as params
import PyPDF2
import os
import chromadb
from sentence_transformers import SentenceTransformer
from gb_assistant.simple_model.chroma import setup_database
from gb_assistant.simple_model.bucket import download_blob


game_file = params.GAME_NAME + ".pdf"
abs_path = os.path.join(os.getcwd(), "raw_data", game_file)
#abs_path = "/Users/alayadi/code/Knolli14/gb-quickstart-assistant/raw_data/3 secrets.pdf"

def load_model():
    """Instanciate the text generation model"""
    qa_pipeline = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")
    return qa_pipeline


def extract_text_from_pdf(pdf_path):
    """Extract text from PDF"""
    with open(pdf_path, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        return text

def load_llm():
    """Loads the final LLM."""
    model_name = "google/flan-t5-small"
    qa_pipe = pipeline("text2text-generation", model=model_name)
    return qa_pipe


def answer_question(model, question:str):
    """Answer the question passed as input"""
    vector_store_path = "/Users/kirillkorzh/code/Knolli14/gb-quickstart-assistant/vector_store"  # Update this path to your PDF directory
    client = chromadb.PersistentClient(vector_store_path)
    collection = client.get_collection(
        name="gb-assistant-complete"
        )

    # Load the LLM
    qa_pipe = model

    # Test the LLM with a sample query
    query = "What are the rules for scoring in this game?"
    embed_model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
    embedded_query = embed_model.encode(query)
    query_results = collection.query(query_embeddings=embedded_query,n_results=3)

    context = "\n\n".join(query_results["documents"][0])
    prompt = context+" "+query
    response = qa_pipe(prompt, max_length=100)

    return response

# new by Olli
def create_answer(model, query, gametitle):

    store_path = "path/to/store"
    game_chunks = download_blob("use params", gametitle+".pdf")

    vindex = setup_database(store_path, gametitle, game_chunks)

    embed_model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
    embedded_query = embed_model.encode(query)

    query_results = vindex.query(query_embeddings=embedded_query,n_results=3)

    context = "\n\n".join(query_results["documents"][0])
    prompt = context+" "+query
    response = model(prompt, max_length=100)

    return response

print(answer_question(load_model(),"how to win?"))
