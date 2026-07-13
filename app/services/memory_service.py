from sqlalchemy.orm import Session

from app.database.crud import save_message, get_messages


def add_message(
    db: Session,
    session_id: str,
    role: str,
    content: str,
):
    save_message(
        db=db,
        session_id=session_id,
        role=role,
        content=content,
    )


def get_history(
    db: Session,
    session_id: str,
):
    return get_messages(
        db=db,
        session_id=session_id,
    )