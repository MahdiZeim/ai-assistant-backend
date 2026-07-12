import ollama


def ask_mistral(message: str) -> str:
    response = ollama.chat(
        model="llama3.2:1b",
        messages=[
            {
                "role": "user",
                "content": message,
            }
        ],
    )

    return response["message"]["content"]