from sentence_transformers import SentenceTransformer
from app.utils.config import EMBEDDING_MODEL

model = SentenceTransformer(EMBEDDING_MODEL)

def generate_embeddings(texts):

    embeddings = model.encode(texts)
    return embeddings