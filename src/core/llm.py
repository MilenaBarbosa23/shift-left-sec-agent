"""Inicialização e configuração do cliente LLM (ChatGroq) via LangChain."""

import sys
from pathlib import Path
from typing import Optional

# Garantir que a raiz do projeto esteja no sys.path para execução direta como script
_root_dir = str(Path(__file__).resolve().parent.parent.parent)
if _root_dir not in sys.path:
    sys.path.insert(0, _root_dir)

from langchain_groq import ChatGroq
from src.core.config import settings


def get_llm(
    api_key: Optional[str] = None,
    model_name: Optional[str] = None,
    temperature: Optional[float] = None,
    max_tokens: Optional[int] = 8192,
) -> ChatGroq:
    """
    Retorna uma instância configurada do ChatGroq.

    Args:
        api_key: Chave da API do Groq (opcional, utiliza settings.GROQ_API_KEY por padrão).
        model_name: Nome do modelo (opcional, utiliza settings.MODEL_NAME por padrão).
        temperature: Temperatura de amostragem (opcional, utiliza settings.DEFAULT_TEMPERATURE por padrão).
        max_tokens: Limite máximo de tokens na resposta (padrão: 8192).

    Returns:
        ChatGroq: Instância configurada pronta para uso com LangChain.

    Raises:
        ValueError: Caso a chave do Groq não tenha sido informada nem encontrada no ambiente.
    """
    groq_key = api_key or settings.GROQ_API_KEY
    if not groq_key or not groq_key.strip():
        raise ValueError(
            "GROQ_API_KEY não foi encontrada! "
            "Defina sua chave no arquivo .env (GROQ_API_KEY=sua_chave) ou passe-a diretamente."
        )

    return ChatGroq(
        groq_api_key=groq_key.strip(),
        model_name=model_name or settings.MODEL_NAME,
        temperature=settings.DEFAULT_TEMPERATURE if temperature is None else temperature,
        max_tokens=max_tokens,
    )


def smoke_test(api_key: Optional[str] = None) -> bool:
    """
    Executa um teste rápido de fumaça (smoke test) para validar a conectividade e autenticação com o Groq.

    Returns:
        bool: True se a chamada foi bem sucedida, False caso contrário.
    """
    print("Iniciando teste de fumaça com Groq...")
    try:
        llm = get_llm(api_key=api_key)
        print(f"Modelo configurado: {llm.model_name} (temperature={llm.temperature})")
        print("Enviando requisição de teste para a API do Groq...")
        
        response = llm.invoke("Responda apenas 'CONEXAO_OK' para confirmar conectividade.")
        content = response.content.strip() if hasattr(response, "content") else str(response)
        
        print(f"Resposta recebida do Groq: {content}")
        print("✅ Teste de fumaça concluído com sucesso!")
        return True
    except ValueError as ve:
        print(f"⚠️ Erro de configuração: {ve}", file=sys.stderr)
        return False
    except Exception as e:
        print(f"❌ Falha na conexão/autenticação com o Groq: {e}", file=sys.stderr)
        return False


if __name__ == "__main__":
    success = smoke_test()
    sys.exit(0 if success else 1)
