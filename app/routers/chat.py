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

from app.services.chat_service import chat as chat_service

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
    """
    Receive chat requests and delegate
    the business logic to ChatService.
    """

    # Log the incoming request.
    logger.info(
        f"Chat request received: {req.session_id}"
    )

    # Delegate all business logic to ChatService.
    response = chat_service(
        db=db,
        session_id=req.session_id,
        message=req.message,
    )

    # Log successful completion.
    logger.info(
        "AI response generated successfully."
    )

    return response