from fastapi import FastAPI

from app.database.database import Base, engine
from app.models.message import Message
from app.routers.chat import router as chat_router


app = FastAPI()

Base.metadata.create_all(bind=engine)


app.include_router(chat_router)


@app.get("/")
def home():
    return {
        "status": "AI Assistant is running 🚀"
    }