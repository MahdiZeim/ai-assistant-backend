from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class ChatRequest(BaseModel):
    message: str

@app.get("/")
def home():
    return {"status": "AI Assistant is running 🚀"}

@app.post("/chat")
def chat(req: ChatRequest):
    return {
        "user_message": req.message,
        "ai_response": "فعلاً در مرحله تست هستیم 😄"
    }