from fastapi import FastAPI
from fastapi import Depends

from pydantic import BaseModel

from sqlalchemy.orm import Session

from app.services.ollama_service import ask_llm
from app.services.memory_service import (
    add_message,
    get_history,
)

from app.database.database import Base, engine
from app.database.database import get_db
from app.models.message import Message

app = FastAPI()

Base.metadata.create_all(bind=engine)

class ChatRequest(BaseModel):
    session_id: str
    message: str

@app.get("/")
def home():
    return {"status": "AI Assistant is running 🚀"}


@app.post("/chat")
def chat(
    req: ChatRequest,
    db: Session = Depends(get_db),
):
    print("message sent. waiting for response")
    add_message(
        db=db,
        session_id=req.session_id,
        role="user",
        content=req.message,
    )

    history = get_history(
        db=db,
        session_id=req.session_id,
    )

    answer = ask_llm(history)

    add_message(
        db=db,
        session_id=req.session_id,
        role="assistant",
        content=answer,
    )

    return {
        "user_message": req.message,
        "ai_response": answer,
    }