from sqlalchemy.orm import Session

from app.models.message import Message


def save_message(db: Session, session_id: str, role: str, content: str):
    message = Message(
        session_id=session_id,
        role=role,
        content=content,
    )

    db.add(message)
    db.commit()


def get_messages(db: Session, session_id: str):
    messages = (
        db.query(Message)
        .filter(Message.session_id == session_id)
        .order_by(Message.id)
        .all()
    )

    return [
        {
            "role": m.role,
            "content": m.content,
        }
        for m in messages
    ]