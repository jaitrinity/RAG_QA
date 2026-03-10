from fastapi import APIRouter, UploadFile, File
import shutil
import os
import ipdb

from app.services.document_service import process_pdf
from app.utils.config import PDF_FOLDER

router = APIRouter()

@router.post("/upload")

async def upload_pdf(file: UploadFile = File(...)):
    # ipdb.set_trace()
    path = f"{PDF_FOLDER}/{file.filename}"

    with open(path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    chunks = process_pdf(path)

    return {"message": "PDF processed", "chunks": chunks}