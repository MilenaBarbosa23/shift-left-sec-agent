# Planejamento do Projeto - Shift Left Sec Agent

**Disciplina:** GAC126 - Programação Aplicada com Suporte de IA (PASIA)  
**Período:** 2026-2  
**Docente:** Julio César Alves  
**Equipe:** Nicolas e Milena  

Este documento registra as decisões de arquitetura, a divisão de responsabilidades e o detalhamento técnico de cada etapa para a implementação do **Shift Left Sec Agent**, cobrindo o cronograma da Fase 1 e da Fase 2.

---

## 🎯 Resumo das Decisões de Arquitetura

| Decisão | Escolha Definida | Justificativa / Detalhe Técnico |
| :--- | :--- | :--- |
| **Interface do Usuário** | **Streamlit** | Prototipação rápida, suporte nativo a upload de arquivos, exibição lado a lado (original vs. injetado) e download direto. |
| **Provedor de LLM** | **Groq (Fixo)** | Alta velocidade de inferência via API com suporte a modelos como `llama-3.3-70b-versatile` ou `mixtral-8x7b-32768` através de `langchain-groq`. |
| **Formato de Injeção** | **Injeção Contextual (Opção B)** | Os riscos e os Requisitos Não Funcionais (RNFs) de segurança serão injetados diretamente abaixo de cada requisito funcional correspondente. |
| **Parsing de Documentos** | **PyMuPDF + Leitura Nativa** | Extração de texto de PDF com `pymupdf` (fitz) e leitura UTF-8 para arquivos `.md` e `.txt`. |
| **Framework de IA** | **LangChain (LCEL)** | Orquestração de prompts, parser de saídas e conexão com Groq. |

---

## 👥 Matriz de Responsabilidades

| Módulo / Tarefa | Responsável Principal | Apoio / Revisão |
| :--- | :--- | :--- |
| 1. Configuração do Ambiente e Repositório | **Nicolas** | Milena |
| 2. Módulo de Parsing (MD, TXT, PDF) | **Milena** | Nicolas |
| 3. Conexão e Cliente Groq via LangChain | **Nicolas** | Milena |
| 4. Engenharia de Prompts (Análise de Riscos) | **Milena** | Nicolas |
| 5. Construção da Interface Web (Streamlit) | **Nicolas & Milena** | Ambos |
| 6. Mapeamento de Critérios OWASP ASVS | **Milena** | Nicolas |
| 7. Motor de Injeção Contextual de Segurança | **Nicolas** | Milena |
| 8. Exportação e Visualização de Diff | **Milena** | Nicolas |
| 9. Casos de Teste, Avaliação e Documentação | **Nicolas & Milena** | Ambos |

---

## 📋 Fase 1: MVP e Extração Básica (28/10 a 16/11)

### 1. Configuração do Ambiente e Estrutura do Projeto
* **Responsável:** Nicolas
* **Como deve ser executado:**
  1. Criar ambiente virtual Python (`python -m venv .venv`).
  2. Gerar `requirements.txt` contendo:
     - `streamlit`
     - `langchain`
     - `langchain-groq`
     - `pymupdf`
     - `python-dotenv`
     - `pydantic`
  3. Criar `.env.example` com a variável `GROQ_API_KEY=` e garantir que o `.env` esteja no `.gitignore`.
  4. Estruturar o projeto no padrão:
     ```text
     shift-left-sec-agent/
     ├── .env.example
     ├── .gitignore
     ├── README.md
     ├── planejamentos.md
     ├── requirements.txt
     ├── examples/                 # Arquivos de exemplo para teste (.md, .txt, .pdf)
     └── src/
         ├── __init__.py
         ├── core/                 # Configurações e cliente Groq
         │   ├── __init__.py
         │   ├── config.py
         │   └── llm.py
         ├── parsers/              # Extração de texto
         │   ├── __init__.py
         │   └── extractor.py
         ├── agent/                # Prompts e chains do LangChain
         │   ├── __init__.py
         │   ├── prompts.py
         │   └── chains.py
         └── ui/                   # Interface Streamlit
             └── app.py
     ```

### 2. Módulo de Ingestão e Parsing de Documentos
* **Responsável:** Milena
* **Como deve ser executado:**
  1. Em `src/parsers/extractor.py`, criar a função principal `extract_text(uploaded_file) -> str`.
  2. Implementar suporte a 3 extensões:
     - `.md` e `.txt`: decodificação direta de bytes para string via UTF-8.
     - `.pdf`: abertura com `pymupdf` (`fitz.open(stream=..., filetype="pdf")`), iterando pelas páginas para extrair texto mantendo quebras de parágrafo.
  3. Adicionar validações: lançamento de exceções claras caso o documento esteja vazio ou seja incompatível.
  4. Criar scripts de teste simples na pasta `examples/` com documentos com e sem formatação.

### 3. Conexão com a LLM (LangChain + Groq)
* **Responsável:** Nicolas
* **Como deve ser executado:**
  1. Em `src/core/config.py`, carregar chaves e variáveis com `python-dotenv` (ex: `GROQ_API_KEY`, `MODEL_NAME="llama-3.3-70b-versatile"`).
  2. Em `src/core/llm.py`, instanciar o modelo via `ChatGroq`:
     ```python
     ChatGroq(
         temperature=0.2,
         model_name="llama-3.3-70b-versatile",
         groq_api_key=settings.GROQ_API_KEY
     )
     ```
  3. Implementar um teste rápido de fumaça para garantir que a autenticação no Groq responde adequadamente.

### 4. Engenharia de Prompts e Chain de Identificação de Riscos (MVP)
* **Responsável:** Milena
* **Como deve ser executado:**
  1. Em `src/agent/prompts.py`, escrever o prompt de sistema que instrui o Groq a atuar como Auditor Sênior de Cibersegurança em Arquitetura de Software.
  2. O prompt deve instruir o modelo a ler cada seção/requisito do documento e identificar:
     - Falhas arquiteturais potenciais.
     - Vulnerabilidades lógicas (falta de autenticação, ausência de rate limit, dados sensíveis em trânsito, etc.).
     - Classificação de criticidade (Crítico, Alto, Médio, Baixo).
  3. Em `src/agent/chains.py`, montar a chain com LCEL (`analysis_prompt | llm | StrOutputParser()`).

### 5. Interface Inicial no Streamlit (Upload e Análise)
* **Responsável:** Nicolas & Milena (Conjunto)
* **Como deve ser executado:**
  1. Em `src/ui/app.py`, configurar o layout da aplicação (`st.set_page_config(layout="wide")`).
  2. Criar a barra lateral com instruções de uso e campo opcional para informar a chave da API do Groq (caso o usuário não use arquivo `.env`).
  3. Área central:
     - `st.file_uploader` aceitando `.md`, `.txt`, `.pdf`.
     - Painel expansível para conferência do texto extraído.
     - Botão `st.button("🔍 Analisar Riscos de Segurança")` com `st.spinner("Analisando com Groq...")`.
     - Exibição do relatório de vulnerabilidades gerado pelo modelo.

---

## 🛡️ Fase 2: Refinamento Agêntico e Injeção de Segurança (17/11 a 30/11)

### 6. Padrões de Mercado: Alinhamento com OWASP ASVS
* **Responsável:** Milena
* **Como deve ser executado:**
  1. Estruturar diretrizes baseadas no **OWASP ASVS v4.0** (Authentication, Access Control, Data Protection, Stored Cryptography, Communications).
  2. Ajustar os prompts para que a IA justifique cada risco e cada sugestão citando diretamente a categoria e o controle do OWASP ASVS correspondente (ex: `[OWASP ASVS V2 - Authentication]`).
  3. Garantir consistência nas nomenclaturas de segurança e boas práticas de mitigação.

### 7. Motor de Injeção Contextual de Requisitos de Segurança (Opção B)
* **Responsável:** Nicolas
* **Como deve ser executado:**
  1. Desenvolver uma chain especializada de reescrita/enriquecimento em `src/agent/chains.py`.
  2. A chain recebe o documento original e o relatório de análise e produz uma nova versão do documento onde:
     - O texto original de cada requisito funcional é preservado.
     - Logo abaixo de cada requisito vulnerável, é injetado um bloco destacado, por exemplo:
       ```markdown
       > 🛡️ **Segurança & Mitigação (Shift Left):**
       > - **RNF-SEC-XX:** O sistema deve implementar autenticação multifator (MFA) conforme OWASP ASVS V2.
       > - **Mitigação Recomendada:** Utilizar protocolo OpenID Connect / OAuth2 com tokens JWT assinados com chave assimétrica (RS256).
       ```
  3. Validar se o documento de saída mantém a formatação Markdown e legibilidade para o desenvolvedor.

### 8. Exportação do Documento Atualizado e Comparativo (Diff)
* **Responsável:** Milena
* **Como deve ser executado:**
  1. Criar visualização comparativa na interface Streamlit:
     - Abas ou colunas lado a lado: **Documento Original** vs. **Documento Enriquecido com Segurança**.
  2. Implementar botões de download:
     - `st.download_button` para exportar o novo arquivo em `.md` e `.txt`.
     - (Opcional se houver tempo hábil) conversão para `.pdf`.

### 9. Bateria de Testes, Validação e Documentação Final
* **Responsável:** Nicolas & Milena (Conjunto)
* **Como deve ser executado:**
  1. Criar 3 documentos de requisitos reais/fictícios na pasta `examples/`:
     - Exemplo 1: Sistema de Autenticação e Gestão de Usuários (com falhas de senha e sessão).
     - Exemplo 2: Plataforma de E-commerce / Gateway de Pagamento (com falhas de controle de acesso e idempotência).
     - Exemplo 3: Prontuário Médico / Gestão de Dados Pessoais (com falhas de privacidade e LGPD).
  2. Avaliar a qualidade dos requisitos injetados pelo Groq em cada cenário.
  3. Atualizar o `README.md` com:
     - Instruções claras de instalação e execução (`streamlit run src/ui/app.py`).
     - Tabela dos prompts mais relevantes desenvolvidos (requisito PASIA).
     - Prints e demonstração do funcionamento da ferramenta.
