from fastapi import FastAPI

from app.database.database import Base, engine
from app.models.message import Message
from app.routers.chat import router as chat_router
from app.routers.health import router as health_router
from app.version import __version__

app = FastAPI(
    title="AI Assistant API",
    description="A FastAPI backend powered by Ollama.",
    version=__version__,
)

Base.metadata.create_all(bind=engine)


app.include_router(chat_router)
app.include_router(health_router)

@app.get("/")
def home():
    return {
        "status": "AI Assistant is running 🚀"
    }