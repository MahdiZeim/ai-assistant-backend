from fastapi import FastAPI
from pydantic import BaseModel

from app.services.ollama_service import ask_llm
from app.services.memory_service import (
    add_message,
    get_history
)

app = FastAPI()


class ChatRequest(BaseModel):
    message: str


@app.get("/")
def home():
    return {"status": "AI Assistant is running 🚀"}


@app.post("/chat")
def chat(req: ChatRequest):

    add_message("user", req.message)

    answer = ask_llm(
        get_history()
    )

    add_message("assistant", answer)

    return {
        "user_message": req.message,
        "ai_response": answer
    }