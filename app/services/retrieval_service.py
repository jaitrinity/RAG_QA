from app.services.embedding_service import generate_embeddings
from app.services.vector_service import search

def retrieve_documents(query):

    embedding = generate_embeddings([query])[0]
    # print(f"Generated embedding for query: {embedding}")
    results, scores = search(embedding)

    return results, scores