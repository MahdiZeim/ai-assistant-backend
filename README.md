# AI Assistant Backend 🚀

A local AI assistant backend built with **FastAPI** and **Ollama**, providing an API interface for interacting with local Large Language Models (LLMs).

The project demonstrates how to build a scalable backend service that connects a web API to a locally running AI model.

## Features

* ⚡ FastAPI-based REST API
* 🤖 Local LLM integration using Ollama
* 🧠 Conversation memory support
* 🔄 Configurable AI model support
* 📚 Automatic API documentation with Swagger UI
* 🐍 Clean Python project structure

## Tech Stack

* **Python**
* **FastAPI**
* **Uvicorn**
* **Ollama**
* **Llama 3.2 1B**
* **Pydantic**

## Project Architecture

```
ai-assistant-backend/
│
├── app/
│   └── services/
│       ├── ollama_service.py
│       └── memory_service.py
│
├── main.py
├── requirements.txt
└── README.md
```

## How It Works

```
Client
  |
  | HTTP Request
  ↓
FastAPI Backend
  |
  ↓
Conversation Memory
  |
  ↓
Ollama Service
  |
  ↓
Local LLM (Llama 3.2 1B)
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/MahdiZeim/ai-assistant-backend.git

cd ai-assistant-backend
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Install Ollama

Install Ollama from:

https://ollama.com

Then download the model:

```bash
ollama pull llama3.2:1b
```

## Running the Application

Start the FastAPI server:

```bash
python -m uvicorn main:app --reload
```

The API will be available at:

```
http://127.0.0.1:8000
```

Swagger documentation:

```
http://127.0.0.1:8000/docs
```

## API Usage

### Chat Endpoint

**POST**

```
/chat
```

Request:

```json
{
  "message": "Hello"
}
```

Response:

```json
{
  "user_message": "Hello",
  "ai_response": "Hello! How can I help you today?"
}
```

## Future Improvements

* [ ] Persistent conversation storage with SQLite
* [ ] User sessions
* [ ] Authentication system
* [ ] Frontend chat interface
* [ ] Document-based question answering (RAG)
* [ ] Support for multiple AI models

## License

This project is for learning and development purposes.
