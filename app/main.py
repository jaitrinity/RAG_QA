from fastapi import FastAPI
from app.api import upload_api, query_api

app = FastAPI(title="Agentic RAG System")

app.include_router(upload_api.router)
app.include_router(query_api.router)