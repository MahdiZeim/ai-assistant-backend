import os

from dotenv import load_dotenv

load_dotenv()


class Settings:
    """
    Application configuration.
    """

    OLLAMA_MODEL = os.getenv(
        "OLLAMA_MODEL",
        "llama3.2:1b",
    )

    OLLAMA_HOST = os.getenv(
        "OLLAMA_HOST",
        "http://127.0.0.1:11434",
    )


settings = Settings()