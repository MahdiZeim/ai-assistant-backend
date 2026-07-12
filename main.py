from fastapi import FastAPI
from pydantic import BaseModel

from app.services.ollama_service import ask_mistral

app = FastAPI()


class ChatRequest(BaseModel):
    message: str


@app.get("/")
def home():
    return {"status": "AI Assistant is running 🚀"}


@app.post("/chat")
def chat(req: ChatRequest):
    print("Received:", req.message)
    
    answer = ask_mistral(req.message)

    return {
        "user_message": req.message,
        "ai_response": answer
    }