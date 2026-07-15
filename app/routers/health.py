"""
Health check endpoints.
"""

from fastapi import APIRouter

from app.core.config import settings

from app.version import __version__

router = APIRouter(
    prefix="/health",
    tags=["Health"],
)


@router.get("/")
def health():
    """
    Return the application health status.
    """

    return {
        "status": "healthy",
        "database": "connected",
        "llm_model": settings.OLLAMA_MODEL,
        "version":  __version__,
    }