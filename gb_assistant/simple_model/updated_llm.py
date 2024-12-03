import os
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer
from transformers import pipeline
import chromadb


def load_llm():
    """Loads the final LLM."""
    model_name = "google/flan-t5-small"
    qa_pipe = pipeline("text2text-generation", model=model_name)
    return qa_pipe

# Example usage
if __name__ == "__main__":
    # Specify your PDF folder path
    vector_store_path = "/Users/kirillkorzh/code/Knolli14/gb-quickstart-assistant/vector_store"  # Update this path to your PDF directory
    client = chromadb.PersistentClient(vector_store_path)
    collection = client.get_collection(
        name="gb-assistant-complete"
        )
    print(collection.count())
    # Load the LLM
    qa_pipe = load_llm()

    # Test the LLM with a sample query
    query = "What did King of Babylon do?"
    embed_model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
    embedded_query = embed_model.encode(query)
    query_results = collection.query(query_embeddings=embedded_query,n_results=3)
    print(query_results)
    """context = "\n\n".join(query_results["documents"][0])
    prompt = context+" "+query
    response = qa_pipe(prompt, max_length=100)
    print(f"LLM Response: {response[0]['generated_text']}")"""
