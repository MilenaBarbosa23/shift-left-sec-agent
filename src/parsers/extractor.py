"""Módulo de extração de texto para documentos Markdown (.md), texto simples (.txt) e PDF (.pdf)."""

import os
from pathlib import Path
from typing import Any, Union
try:
    import pymupdf as fitz  # PyMuPDF moderno
except ImportError:
    import fitz  # Fallback legado


SUPPORTED_EXTENSIONS = {".md", ".txt", ".pdf"}


class DocumentExtractionError(Exception):
    """Exceção levantada quando ocorre um erro na extração do documento."""
    pass


def extract_text(uploaded_file: Any) -> str:
    """
    Extrai o conteúdo textual de arquivos .md, .txt ou .pdf.

    Suporta:
    - Streamlit UploadedFile
    - Objetos do tipo arquivo (com atributos .name e .read()/.getvalue())
    - Caminhos de arquivo (str ou Path)

    Args:
        uploaded_file: Arquivo enviado ou caminho para o arquivo.

    Returns:
        str: Texto extraído e normalizado do documento.

    Raises:
        ValueError: Caso o formato seja inválido ou o arquivo esteja vazio.
        DocumentExtractionError: Caso ocorra falha na decodificação ou leitura do PDF.
    """
    if uploaded_file is None:
        raise ValueError("Nenhum arquivo foi fornecido para extração.")

    # Obter nome do arquivo e extensão
    if isinstance(uploaded_file, (str, Path)):
        file_path = Path(uploaded_file)
        if not file_path.exists():
            raise FileNotFoundError(f"Arquivo não encontrado: {file_path}")
        filename = file_path.name
        content_bytes = file_path.read_bytes()
    else:
        filename = getattr(uploaded_file, "name", "")
        if hasattr(uploaded_file, "getvalue"):
            content_bytes = uploaded_file.getvalue()
        elif hasattr(uploaded_file, "read"):
            content_bytes = uploaded_file.read()
            if hasattr(uploaded_file, "seek"):
                uploaded_file.seek(0)
        else:
            raise ValueError("Objeto de arquivo não reconhecido.")

    if not content_bytes or len(content_bytes) == 0:
        raise ValueError("O documento fornecido está vazio.")

    # Validar extensão
    ext = Path(filename).suffix.lower()
    if ext not in SUPPORTED_EXTENSIONS:
        raise ValueError(
            f"Formato de arquivo incompatível: '{ext}'. Extensões suportadas: {', '.join(sorted(SUPPORTED_EXTENSIONS))}."
        )

    # Extração de texto para .md e .txt
    if ext in {".md", ".txt"}:
        try:
            text = content_bytes.decode("utf-8")
        except UnicodeDecodeError:
            try:
                text = content_bytes.decode("latin-1")
            except Exception as e:
                raise DocumentExtractionError(f"Erro ao decodificar arquivo de texto: {e}") from e

        cleaned_text = text.strip()
        if not cleaned_text:
            raise ValueError("O documento contém apenas espaços em branco.")
        return cleaned_text

    # Extração de texto para .pdf com PyMuPDF
    if ext == ".pdf":
        try:
            doc = fitz.open(stream=content_bytes, filetype="pdf")
        except Exception as e:
            raise DocumentExtractionError(f"Falha ao abrir arquivo PDF: {e}") from e

        try:
            pages_text = []
            for page_num in range(len(doc)):
                page = doc[page_num]
                page_str = page.get_text("text")
                if page_str and page_str.strip():
                    pages_text.append(page_str.strip())
        finally:
            doc.close()

        extracted = "\n\n".join(pages_text).strip()
        if not extracted:
            raise ValueError(
                "Nenhum texto pôde ser extraído do PDF. O arquivo pode conter apenas imagens digitalizadas ou estar vazio."
            )

        return extracted

    raise ValueError(f"Extensão não tratada: {ext}")
