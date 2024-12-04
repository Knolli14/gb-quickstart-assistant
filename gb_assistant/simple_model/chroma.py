import chromadb


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
