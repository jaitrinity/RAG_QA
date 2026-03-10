import openai
from app.utils.config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY


def generate_answer(prompt):

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response["choices"][0]["message"]["content"]