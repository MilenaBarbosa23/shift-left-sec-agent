"""Construção de chains de análise de risco e enriquecimento contextual via LangChain."""

import sys
from pathlib import Path
from typing import Optional

# Garantir sys.path para importações locais
_root_dir = str(Path(__file__).resolve().parent.parent.parent)
if _root_dir not in sys.path:
    sys.path.insert(0, _root_dir)

from langchain_core.output_parsers import StrOutputParser
from src.agent.prompts import SECURITY_AUDIT_PROMPT
from src.core.llm import get_llm


def create_security_analysis_chain(
    api_key: Optional[str] = None,
    model_name: Optional[str] = None,
    temperature: Optional[float] = None,
):
    """
    Cria a chain de auditoria de segurança utilizando LCEL.

    Args:
        api_key: Chave do Groq opcional.
        model_name: Nome do modelo opcional.
        temperature: Temperatura do modelo.

    Returns:
        Runnable: Chain compilada pronta para invocação.
    """
    llm = get_llm(api_key=api_key, model_name=model_name, temperature=temperature)
    chain = SECURITY_AUDIT_PROMPT | llm | StrOutputParser()
    return chain


def analyze_security_risks(
    document_text: str,
    api_key: Optional[str] = None,
    model_name: Optional[str] = None,
) -> str:
    """
    Executa a análise de riscos de segurança sobre o texto do documento fornecido.

    Args:
        document_text: Conteúdo textual dos requisitos.
        api_key: Chave da API do Groq (opcional, fallback para settings.GROQ_API_KEY).
        model_name: Modelo a ser utilizado (opcional).

    Returns:
        str: Relatório formatado em Markdown com as vulnerabilidades e recomendações.
    """
    if not document_text or not document_text.strip():
        raise ValueError("O texto do documento está vazio.")

    chain = create_security_analysis_chain(api_key=api_key, model_name=model_name)
    response = chain.invoke({"document_text": document_text})
    return response
