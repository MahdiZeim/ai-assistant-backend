import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    OLLAMA_MODEL = os.getenv(
        "OLLAMA_MODEL",
        "llama3.2:1b"
    )


settings = Settings()