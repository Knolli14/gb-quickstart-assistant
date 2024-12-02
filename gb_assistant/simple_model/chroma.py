import chromadb
import os

def setup_chromadb(collection_name:str, embeddings, metadatas, documents):
    client = chromadb.PersistentClient(path="/Users/alayadi/code/Knolli14/gb-quickstart-assistant/vector_store")
    collection = client.create_collection(name=collection_name)
    collection.add(
        embeddings=embeddings,
        metadatas=metadatas,
        documents=documents,
        ids=[str(i) for i in range(len(embeddings))],
        )
    return collection

def get_collection():
    client = chromadb.PersistentClient(path="/Users/alayadi/code/Knolli14/gb-quickstart-assistant/vector_store")
    collection = client.get_collection(name='testset')
    return collection
