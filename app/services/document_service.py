import os

from app.document_processing.pdf_loader import extract_text_from_pdf
from app.document_processing.chunker import chunk_text
from app.services.embedding_service import generate_embeddings
from app.services.vector_service import create_index, add_vectors


def process_pdf(file_path):

    text = extract_text_from_pdf(file_path)

    chunks = chunk_text(text)

    embeddings = generate_embeddings(chunks)

    dim = len(embeddings[0])

    create_index(dim)

    add_vectors(embeddings, chunks)

    return len(chunks)