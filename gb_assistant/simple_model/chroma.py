import chromadb


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
    collection = client.get_collection()
    return collection




#new by Olli
def create_index(game_chunks, collection):
    for chunk in game_chunks:
        collection.add(
            ids=chunk[0],
            documents=chunk[1],
            embeddings=chunk[2]
        )

def create_collection(path, title, dfunc="cosine"):

    client = chromadb.PersistentClient(path)
    collection = client.get_or_create_collection(
        name=title,
        metadata={"hnsw:space": dfunc}
    )
    return collection


def setup_database(path, title, game_chunks, dfunc="cosine"):

    collection = create_collection(
        path=path,
        title=title
    )

    vindex = create_index(game_chunks, collection)

    return vindex
