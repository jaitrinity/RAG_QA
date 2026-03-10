# RAG_QA
## Liberary Install
```bash
pip install -r requirements.txt
```

## Run backend (Fast API) at Terminal one
```bash
uvicorn app.main:app --reload
```

## Run frontend (Streamlit) at Terminal two
```bash
streamlit run streamlit_app/app.py
```

# Agent Decision Logic
```bash
User Question
      │
      ▼
   Agent Reasoning
      │
      ├── Retrieve context from Vector DB
      │         │
      │         ▼
      │     Relevant Chunks
      │         │
      │         ▼
      │      LLM Answer
      │
      └── Answer directly using LLM
```

# Core Features
## 1. PDF Upload
Users can upload PDF documents through the Streamlit UI.

## 2. Text Extraction
The system extracts text from the uploaded PDF.

Libraries that can be used:
- PyMuPDF
- pdfplumber
- PyPDF

## 3. Text Chunking
Large documents are split into smaller chunks using:
> RecursiveCharacterTextSplitter
Chunking helps improve embedding quality and retrieval performance.

## 4. Embedding Generation
Each chunk is converted into a **vector embedding**.

Possible embedding models:
- HuggingFace Embeddings
- OpenAI Embeddings
- SentenceTransformers

## 5. Vector Database
Embeddings are stored in a Vector Database.

Supported vector stores:
- FAISS
- ChromaDB

## 6. Vector Search (Retrieval)
When a question is asked:
1. The query is converted to an embedding
2. Similar chunks are retrieved from the vector database

## 7. Agent Reasoning
The Agent decides:
- whether retrieval is required
- or if the LLM can answer directly

Agent reasoning can be implemented using:
- LangChain Agents
- Tool Calling
- Function Calling

## 8. Answer Generation
The LLM generates the final answer using:
- Retrieved context (RAG)
- Agent reasoning

# System Architecture
```bash
              +--------------------+
              |      Streamlit UI  |
              |--------------------|
              | Upload PDF         |
              | Ask Questions      |
              | Show Agent Steps   |
              +----------+---------+
                         |
                         |
                         ▼
               +------------------+
               |      FastAPI     |
               |------------------|
               | Upload API       |
               | Embedding API    |
               | Retrieval API    |
               | Agent API        |
               +---------+--------+
                         |
                         |
                         ▼
               +------------------+
               |   Document       |
               |   Processing     |
               |------------------|
               | PDF Extraction   |
               | Text Chunking    |
               | Embeddings       |
               +---------+--------+
                         |
                         |
                         ▼
               +------------------+
               |  Vector Database |
               |------------------|
               | FAISS / Chroma   |
               | Similarity Search|
               +------------------+
```