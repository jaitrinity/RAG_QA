from fastapi import APIRouter
from pydantic import BaseModel
import ipdb

from app.agents.rag_agent import agent_answer

router = APIRouter()

class Query(BaseModel):
    question: str


@router.post("/ask")

def ask_question(query: Query):
    # ipdb.set_trace()
    reasoning, context, answer = agent_answer(query.question)

    return {
        "question": query.question,
        "agent_reasoning": reasoning,
        "retrieved_context": context,
        "answer": answer
    }