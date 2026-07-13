from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.services.memory_service import (
    add_message,
    get_history,
)
from app.services.ollama_service import ask_llm

from app.core.logger import logger

router = APIRouter(
    prefix="/chat",
    tags=["Chat"]
)


class ChatRequest(BaseModel):
    session_id: str
    message: str


@router.post("/")
def chat(
    req: ChatRequest,
    db: Session = Depends(get_db),
):

    #print("message sent, waiting for response")
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

    #save message to logger
    logger.info(
    f"Chat request received: {req.session_id}"
    )

    answer = ask_llm(history)

    logger.info(
    "AI response generated successfully"
    )

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