import faiss
import numpy as np
import os
from app.utils.config import VECTOR_DB_PATH

index = None
documents = []

def create_index(dim):

    global index
    index = faiss.IndexFlatL2(dim)

def add_vectors(vectors, texts):

    global documents
    index.add(np.array(vectors).astype("float32"))
    documents.extend(texts)

def search(query_vector, top_k=3):
    # print(f"Searching for query vector: {query_vector} with top_k: {top_k}")
    D, I = index.search(np.array([query_vector]).astype("float32"), top_k)

    results = []
    scores = []

    for idx, dist in zip(I[0], D[0]):
        results.append(documents[idx])
        scores.append(dist)
    # print(f"Search results: {results} with scores: {scores}")
    return results, scores