from fastapi.testclient import TestClient

from main import app
import app.services.ollama_service as ollama_service


client = TestClient(app)


def fake_ask_llm(messages):
    """
    Fake LLM response used during testing.
    """
    return "This is a test response"


def test_home():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["status"] == "AI Assistant is running 🚀"


def test_chat(monkeypatch):
    """
    Verify that the chat endpoint returns
    the mocked AI response.
    """

    monkeypatch.setattr(
        ollama_service,
        "ask_llm",
        fake_ask_llm,
    )

    response = client.post(
        "/chat/",
        json={
            "session_id": "test-session",
            "message": "Hello",
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["user_message"] == "Hello"
    assert data["ai_response"] == "This is a test response"