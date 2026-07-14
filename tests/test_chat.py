import app.routers.chat as chat_router

from fastapi.testclient import TestClient

from main import app
from app.services import ollama_service


client = TestClient(app)


def fake_ask_llm(messages):
    return "This is a test response"


def test_chat(monkeypatch):

    monkeypatch.setattr(
        chat_router,
        "ask_llm",
        fake_ask_llm
    )

    response = client.post(
        "/chat/",
        json={
            "session_id": "test-session",
            "message": "Hello"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["user_message"] == "Hello"

    assert data["ai_response"] == (
        "This is a test response"
    )