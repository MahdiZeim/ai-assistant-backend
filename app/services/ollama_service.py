import ollama
import os

from fastapi import HTTPException
from app.core.config import settings
from app.core.logger import logger

def ask_llm(messages):

    try:

        # Configure Ollama host from application settings.
        os.environ["OLLAMA_HOST"] = settings.OLLAMA_HOST
        
        response = ollama.chat(
            model=settings.OLLAMA_MODEL,
            messages=messages,
        )

        return response["message"]["content"]

    
    except Exception as e:
        logger.error(
        f"Ollama error: {str(e)}"
        )
        
        #raise HTTPException(
            #status_code=500,
            #detail=f"LLM Error: {str(e)}"
        #)