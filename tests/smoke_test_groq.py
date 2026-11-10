"""Script de teste de fumaça (smoke test) para validar conexão com a API do Groq."""

import sys
from pathlib import Path

# Ajustar sys.path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.core.llm import smoke_test

if __name__ == "__main__":
    success = smoke_test()
    sys.exit(0 if success else 1)
