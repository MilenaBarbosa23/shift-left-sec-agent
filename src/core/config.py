"""Gerenciamento de configurações e variáveis de ambiente."""

import os
from pathlib import Path
from dotenv import load_dotenv
from pydantic import BaseModel, Field

# Carregar arquivo .env a partir da raiz do projeto
BASE_DIR = Path(__file__).resolve().parent.parent.parent
ENV_PATH = BASE_DIR / ".env"
load_dotenv(dotenv_path=ENV_PATH)


class Settings(BaseModel):
    """Configurações gerais do projeto carregadas do ambiente."""

    GROQ_API_KEY: str = Field(default_factory=lambda: os.getenv("GROQ_API_KEY", ""))
    MODEL_NAME: str = Field(
        default_factory=lambda: os.getenv("MODEL_NAME", "llama-3.3-70b-versatile")
    )
    DEFAULT_TEMPERATURE: float = Field(
        default_factory=lambda: float(os.getenv("DEFAULT_TEMPERATURE", "0.2"))
    )

    def reload(self) -> None:
        """Recarrega as configurações a partir do arquivo .env ou variáveis de ambiente."""
        load_dotenv(dotenv_path=ENV_PATH, override=True)
        self.GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")
        self.MODEL_NAME = os.getenv("MODEL_NAME", "llama-3.3-70b-versatile")
        self.DEFAULT_TEMPERATURE = float(os.getenv("DEFAULT_TEMPERATURE", "0.2"))


# Instância singleton para uso em todo o projeto
settings = Settings()
