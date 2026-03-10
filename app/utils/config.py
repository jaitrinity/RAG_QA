import os

VECTOR_DB_PATH = "data/vector_store/faiss.index"
PDF_FOLDER = "data/pdfs"
EMBEDDING_MODEL = "all-MiniLM-L6-v2"
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")