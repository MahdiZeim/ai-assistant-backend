import ollama


def ask_llm(messages):
    response = ollama.chat(
        model="llama3.2:1b",
        messages = messages,
    )

    return response["message"]["content"]