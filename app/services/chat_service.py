"""
Chat service.

This module contains the business logic of the chat workflow.
The router should only receive HTTP requests and delegate
the processing to this service.
"""

from sqlalchemy.orm import Session

from app.services.memory_service import (
    add_message,
    get_history,
)

from app.services.ollama_service import ask_llm


def chat(
    db: Session,
    session_id: str,
    message: str,
):
    """
    Process a complete chat request.

    Steps:
    1. Save the user's message.
    2. Load the conversation history.
    3. Send the history to the LLM.
    4. Save the AI response.
    5. Return the final response.
    """

    # Save user's message into the database.
    add_message(
        db=db,
        session_id=session_id,
        role="user",
        content=message,
    )

    # Retrieve the conversation history.
    history = get_history(
        db=db,
        session_id=session_id,
    )

    # Generate a response using the language model.
    answer = ask_llm(history)

    # Store the AI response.
    add_message(
        db=db,
        session_id=session_id,
        role="assistant",
        content=answer,
    )

    # Return the API response.
    return {
        "user_message": message,
        "ai_response": answer,
    }