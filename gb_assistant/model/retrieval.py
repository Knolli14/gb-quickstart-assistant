# Query with metadata filtering
results = collection.query(
    query_embeddings=[[0.1, 0.2, 0.3]],  # Example embedding
    n_results=5,  # Retrieve top 5 results
    where={"file_name": "game_rules.pdf"},  # Filter to only "game_rules.pdf"
    include=["documents", "metadatas"]
)

# Display filtered results
for doc, metadata in zip(results["documents"], results["metadatas"]):
    print(f"Document: {doc}")
    print(f"Metadata: {metadata}")



# Perform an initial query
results = collection.query(
    query_embeddings=[[0.1, 0.2, 0.3]],
    n_results=10,  # Retrieve more results for better re-ranking
    include=["documents", "metadatas"]
)

# Define additional ranking logic (e.g., keyword scoring)
query_keywords = ["scoring", "rules"]
ranked_results = sorted(
    zip(results["documents"], results["metadatas"]),
    key=lambda x: sum(keyword in x[0] for keyword in query_keywords),
    reverse=True
)

# Display re-ranked results
for doc, metadata in ranked_results:
    print(f"Document: {doc}")
    print(f"Metadata: {metadata}")



#Optimizing towards precision
results = collection.query(query_embeddings=[[0.1, 0.2, 0.3]], n_results=3)
#Optimizing towards recall 
results = collection.query(query_embeddings=[[0.1, 0.2, 0.3]], n_results=20)



#Add context to chunks 
chunk_text = f"File: {file_name}, Page: {page_number}\n{text}"



#Query expansion 
query = "scoring rules"
expanded_query = "scoring rules points marks"

# Generate embedding for the expanded query
query = "scoring rules"
expanded_query = "scoring rules points marks"

# Generate embedding for the expanded query
query_embedding = model.encode([expanded_query])
results = collection.query(query_embeddings=query_embedding, n_results=5)


#Merge similar chunks 
# Summarize retrieved documents using GPT
retrieved_texts = " ".join(results["documents"])
summary = language_model.summarize(retrieved_texts)

print("Summary:", summary)
