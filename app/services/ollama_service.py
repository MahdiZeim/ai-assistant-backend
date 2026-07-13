import ollama

from fastapi import HTTPException

def ask_llm(messages):

    try:

        response = ollama.chat(
            model="llama3.2:1b",
            messages=messages,
        )

        return response["message"]["content"]

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=f"LLM Error: {str(e)}"
        )