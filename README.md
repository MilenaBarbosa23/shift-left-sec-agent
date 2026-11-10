# Shift Left Sec Agent

**Disciplina:** GAC126 - Programação Aplicada com Suporte de IA (PASIA)  
**Período:** 2026-2  
**Docente:** Julio César Alves  
**Equipe:** Nicolas e Milena  

---

## 🎯 Missão do Projeto
O **Shift Left Sec Agent** é uma ferramenta interativa desenvolvida para revolucionar a segurança no ciclo de desenvolvimento de software (*DevSecOps*). 

A aplicação recebe documentos de especificação de requisitos de software (em formatos `.md`, `.txt` ou `.pdf`) e utiliza um agente de IA Generativa de alta performance para auditar a especificação *antes* de qualquer linha de código ser escrita. O agente identifica falhas arquiteturais, lacunas lógicas de autenticação/autorização, exposição de dados sensíveis e riscos de conformidade (como LGPD e OWASP), sugerindo mitigações acionáveis na fase de concepção (*Shift Left Security*).

---

## ⚙️ Pilha Tecnológica

| Componente | Tecnologia | Finalidade |
| :--- | :--- | :--- |
| **Linguagem** | Python 3.14+ | Linguagem base do projeto |
| **Interface Web** | Streamlit | UI rápida, responsiva com upload de arquivos e visualização interativa |
| **Provedor de LLM** | Groq (`langchain-groq`) | Inferência de ultra baixa latência com modelos abertos (`openai/gpt-oss-120b`, `qwen/qwen3.8-27b`) |
| **Framework de IA** | LangChain (LCEL) | Orquestração de prompts, cadeias de análise e formatação de saídas |
| **Extração de Documentos** | PyMuPDF (`pymupdf`) | Extração estruturada de texto de documentos PDF, além de suporte nativo a Markdown e TXT |
| **Configuração & Validação** | `python-dotenv` & `pydantic` | Gestão de variáveis de ambiente seguras e tipadas |

---

## 📁 Estrutura do Projeto

```text
shift-left-sec-agent/
├── .env.example              # Modelo de variáveis de ambiente (chaves de API)
├── .gitignore                 # Arquivos ignorados pelo controle de versão (.env, .venv, etc.)
├── README.md                  # Documentação principal da aplicação
├── planejamentos.md           # Decisões arquiteturais, cronograma e divisão de tarefas
├── requirements.txt           # Dependências do projeto
├── examples/                  # Casos de teste e documentos de requisitos reais e fictícios
│   ├── exemplo_requisitos.md  # Exemplo sintético de autenticação e pagamentos
│   ├── exemplo_requisitos.txt # Exemplo de endpoint público de pedidos
│   ├── exemplo_requisitos.pdf # Exemplo em formato PDF
│   └── VerCandidato.md        # Caso real completo (Módulo WeGrano - 14KB)
├── tests/
│   └── smoke_test_groq.py     # Teste de fumaça para validação da conexão com o Groq
└── src/
    ├── __init__.py
    ├── core/                  # Infraestrutura, configurações e conexão LLM
    │   ├── __init__.py
    │   ├── config.py          # Carregamento do .env via Pydantic
    │   └── llm.py             # Instanciação do ChatGroq e smoke tests
    ├── parsers/               # Ingestão de arquivos
    │   ├── __init__.py
    │   └── extractor.py       # Extração de texto para .md, .txt e .pdf (PyMuPDF)
    ├── agent/                 # Engenharia de Prompts e Chains
    │   ├── __init__.py
    │   ├── prompts.py         # Templates de sistema para auditoria Shift Left
    │   └── chains.py          # Chains LCEL de identificação de riscos
    └── ui/                    # Interface gráfica do usuário
        └── app.py             # Aplicação web Streamlit
```

---

## 🚀 Instruções para Instalação e Execução Local

### 1. Clonar o Repositório
```bash
git clone git@github.com:MilenaBarbosa23/shift-left-sec-agent.git
cd shift-left-sec-agent
```

### 2. Criar e Ativar o Ambiente Virtual Python
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Instalar as Dependências
```bash
pip install -r requirements.txt
```

### 4. Configurar as Variáveis de Ambiente
Crie seu arquivo `.env` a partir do modelo de exemplo:
```bash
cp .env.example .env
```
Edite o arquivo `.env` e insira sua chave da API da Groq:
```env
GROQ_API_KEY=gsk_sua_chave_aqui
MODEL_NAME=openai/gpt-oss-120b
```
*(Caso não possua chave, você pode gerá-la gratuitamente em [console.groq.com/keys](https://console.groq.com/keys)).*

### 5. Validar a Conexão com o Groq (Smoke Test)
Execute o teste rápido para garantir que a autenticação está funcionando:
```bash
python tests/smoke_test_groq.py
```
*Saída esperada:* `✅ Teste de fumaça concluído com sucesso!`

### 6. Executar a Aplicação Web
Inicie a interface do Streamlit:
```bash
streamlit run src/ui/app.py
```
A aplicação abrirá automaticamente no navegador no endereço `http://localhost:8501`.

---

## 🗺️ Status do Roadmap

### 📋 Fase 1: MVP e Extração Básica (Concluída ✅)
- [x] **Item 1:** Configuração do ambiente virtual, dependências e estrutura modular do projeto.
- [x] **Item 2:** Módulo de ingestão e parsing de documentos com suporte a `.md`, `.txt` e `.pdf`.
- [x] **Item 3:** Conexão com LLM via LangChain e Groq com validação por teste de fumaça.
- [x] **Item 4:** Engenharia de prompts e chain LCEL inicial de auditoria de segurança.
- [x] **Item 5:** Interface gráfica no Streamlit com upload, conferência de texto e geração de relatório com download em Markdown.

### 🛡️ Fase 2: Refinamento Agêntico e Injeção de Segurança (Em Andamento 🔄)
- [ ] **Item 6:** Mapeamento formal e citação de critérios do **OWASP ASVS v4.0** (V2 Autenticação, V4 Controle de Acesso, etc.).
- [ ] **Item 7:** Motor de **Injeção Contextual de Requisitos de Segurança (Opção B)**, inserindo blocos de mitigação diretamente abaixo de cada requisito funcional vulnerável.
- [ ] **Item 8:** Visualização comparativa lado a lado (Original vs. Enriquecido com Diff) no Streamlit.
- [ ] **Item 9:** Bateria final de testes em múltiplos cenários e documentação dos resultados.

---

## 🤖 Engenharia de Prompts Aplicada (Requisito PASIA)

Conforme diretrizes da disciplina, a tabela abaixo registra os prompts nucleares construídos para o agente:

| Identificador | Finalidade | Estrutura Base / Papel do Agente | Saída Esperada |
| :--- | :--- | :--- | :--- |
| `SECURITY_AUDIT_PROMPT` | Auditoria de segurança Shift Left em requisitos brutos | Atua como Auditor Sênior de Cibersegurança em Arquitetura. Avalia requisitos, detecta falhas arquiteturais/lógicas, categoriza a severidade (Crítico, Alto, Médio, Baixo) e recomenda mitigações preventivas. | Relatório em Markdown com Resumo Executivo tabular, análise item a item e diretrizes gerais. |
