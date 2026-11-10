"""Interface web da aplicação Shift Left Sec Agent construída com Streamlit."""

import os
import sys
from pathlib import Path
import streamlit as st

# Garantir que a raiz do projeto esteja no sys.path
ROOT_DIR = Path(__file__).resolve().parent.parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from src.agent.chains import analyze_security_risks
from src.core.config import settings
from src.parsers.extractor import extract_text, DocumentExtractionError

# 1. Configuração do layout da aplicação
st.set_page_config(
    page_title="Shift Left Sec Agent",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# 2. Barra lateral (Sidebar)
with st.sidebar:
    st.markdown("## 🛡️ Shift Left Sec Agent")
    st.caption("Auditoria preventiva de segurança em requisitos de software.")
    st.divider()

    st.markdown("### 📋 Como usar")
    st.markdown(
        """
        1. **Envie seu documento** de requisitos (`.md`, `.txt` ou `.pdf`).
        2. **Verifique o texto extraído** no painel expansível de conferência.
        3. **Clique em Analisar** para que a IA identifique vulnerabilidades arquiteturais e lógicas.
        4. **Exporte o relatório** com classificações de risco e mitigações recomendadas.
        """
    )
    st.divider()

    st.markdown("### ⚙️ Configurações da LLM")
    
    # Campo opcional para informar a chave da API do Groq
    api_key_input = st.text_input(
        "Chave da API do Groq (Opcional)",
        type="password",
        placeholder="gsk_...",
        help="Caso já esteja configurada no arquivo .env, este campo pode ficar em branco.",
    )

    effective_api_key = api_key_input.strip() if api_key_input.strip() else settings.GROQ_API_KEY

    # Indicador de status da chave
    if effective_api_key:
        st.success("🔑 Chave de API Groq configurada.")
    else:
        st.warning("⚠️ Chave de API não informada. Preencha aqui ou no arquivo .env.")

    # Seleção de modelo e temperatura
    available_models = [
        "openai/gpt-oss-120b",
        "qwen/qwen3.8-27b",
        "openai/gpt-oss-20b",
    ]
    current_default_index = (
        available_models.index(settings.MODEL_NAME)
        if settings.MODEL_NAME in available_models
        else 0
    )

    selected_model = st.selectbox(
        "Modelo Groq",
        options=available_models,
        index=current_default_index,
        help="Selecione o modelo de linguagem para a auditoria de segurança.",
    )

    st.divider()
    st.markdown("### 👥 Equipe")
    st.caption("Projeto PASIA 2026-2 — Nicolas & Milena")


# 3. Área Central
st.title("🛡️ Shift Left Sec Agent")
st.markdown(
    """
    **Análise automatizada de vulnerabilidades em requisitos de software.**  
    Identifique riscos arquiteturais, ausência de controles e falhas lógicas *antes* do início da codificação.
    """
)
st.write("")

# Inicialização de estado da sessão
if "report" not in st.session_state:
    st.session_state["report"] = None
if "last_analyzed_file" not in st.session_state:
    st.session_state["last_analyzed_file"] = None

# Upload de arquivo (.md, .txt, .pdf)
uploaded_file = st.file_uploader(
    "📂 Selecione o arquivo de requisitos para auditoria:",
    type=["md", "txt", "pdf"],
    help="Formatos aceitos: Markdown (.md), Texto simples (.txt) ou Documentos PDF (.pdf).",
)

extracted_text = ""
if uploaded_file is not None:
    # Se trocar de arquivo, limpa o relatório anterior
    if st.session_state["last_analyzed_file"] != uploaded_file.name:
        st.session_state["report"] = None
        st.session_state["last_analyzed_file"] = uploaded_file.name

    try:
        extracted_text = extract_text(uploaded_file)
        
        # Métricas do arquivo
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Arquivo", uploaded_file.name)
        with col2:
            st.metric("Tamanho", f"{uploaded_file.size / 1024:.1f} KB")
        with col3:
            st.metric("Caracteres Extraídos", len(extracted_text))

        # Painel expansível para conferência do texto extraído
        with st.expander("📄 Conferência do Texto Extraído", expanded=False):
            st.text_area(
                "Conteúdo completo extraído do documento:",
                value=extracted_text,
                height=260,
                disabled=True,
            )

    except (ValueError, DocumentExtractionError) as e:
        st.error(f"❌ Erro ao extrair texto do documento: {e}")
        extracted_text = ""
    except Exception as e:
        st.error(f"❌ Ocorreu um erro inesperado na leitura do arquivo: {e}")
        extracted_text = ""

# Botão de Ação para Análise
st.write("")
if extracted_text:
    col_btn, _ = st.columns([2, 5])
    with col_btn:
        start_analysis = st.button(
            "🔍 Analisar Riscos de Segurança",
            type="primary",
            use_container_width=True,
        )

    if start_analysis:
        if not effective_api_key:
            st.error("⚠️ Não foi possível iniciar a análise: Chave da API do Groq não configurada!")
        else:
            with st.spinner("Analisando com Groq..."):
                try:
                    report = analyze_security_risks(
                        document_text=extracted_text,
                        api_key=effective_api_key,
                        model_name=selected_model,
                    )
                    st.session_state["report"] = report
                    st.success("✅ Auditoria de segurança concluída com sucesso!")
                except Exception as ex:
                    st.error(f"❌ Falha durante a análise de segurança: {ex}")

# Exibição do Relatório de Vulnerabilidades
if st.session_state.get("report"):
    st.divider()
    st.markdown("## 📊 Relatório de Auditoria de Segurança")

    # Botão de download do relatório em Markdown
    doc_stem = (
        Path(st.session_state["last_analyzed_file"]).stem
        if st.session_state["last_analyzed_file"]
        else "relatorio"
    )
    st.download_button(
        label="📥 Baixar Relatório (.md)",
        data=st.session_state["report"],
        file_name=f"relatorio_seguranca_{doc_stem}.md",
        mime="text/markdown",
    )

    st.markdown(st.session_state["report"])
