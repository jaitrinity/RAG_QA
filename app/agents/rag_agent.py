from app.services.retrieval_service import retrieve_documents
from app.services.llm_service import generate_answer


THRESHOLD = 1.0   # similarity threshold


def agent_answer(question):

    docs, scores = retrieve_documents(question)

    best_score = scores[0]

    if best_score < THRESHOLD:

        reasoning = "Relevant document context found → retrieving."

        context = "\n".join(docs)

        prompt = f"""
Answer the question using the context.

Context:
{context}

Question:
{question}
"""

        answer = generate_answer(prompt)

        return reasoning, context, answer

    else:

        reasoning = "No strong document match → answering directly."

        answer = generate_answer(question)

        return reasoning, "", answer