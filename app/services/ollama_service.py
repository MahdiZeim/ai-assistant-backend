import ollama

from fastapi import HTTPException

from app.core.config import settings

def ask_llm(messages):

    try:

        response = ollama.chat(
            model=settings.OLLAMA_MODEL,
            messages=messages,
        )

        return response["message"]["content"]

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=f"LLM Error: {str(e)}"
        )