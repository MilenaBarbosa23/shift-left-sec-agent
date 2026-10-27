# Shift Left Sec Agent

**Disciplina:** GAC126 - Programação Aplicada com Suporte de IA (PASIA)  
**Período:** 2026-2  
**Docente:** Julio César Alves  

## 🎯 Missão do Projeto
Desenvolver uma ferramenta (web ou CLI) que recebe documentos de requisitos de software e utiliza um agente de IA Generativa para analisá-los, identificando riscos arquiteturais e injetando automaticamente requisitos não funcionais de cibersegurança e boas práticas de mitigação no documento original. O objetivo é aplicar o conceito de *Shift Left*, inserindo a segurança na fase mais inicial do ciclo de desenvolvimento.

## ⚙️ Pilha de Tecnologia
* **Linguagem / Interface:** Python (com FastAPI para backend ou Streamlit para interface web rápida).
* **Orquestração de IA:** LangChain (para conectar o documento ao modelo e estruturar o "agente treinado").
* **Modelos de IA:** Ollama rodando Qwen (local) ou integração com APIs externas de LLMs.

## 🗺️ Roadmap de Desenvolvimento

O projeto está estruturado em duas fases principais:

### Fase 1 (28/10 a 16/11) - MVP e Extração Básica
* Construção da interface de upload e extração de texto do documento de requisitos (suporte inicial a Markdown, TXT ou PDF).
* Implementação da comunicação básica com a IA, enviando o texto extraído.
* Retorno de uma lista de potenciais vulnerabilidades lógicas e riscos arquiteturais identificados.

### Fase 2 (17/11 a 30/11) - Refinamento Agêntico e Injeção de Segurança
* Refinamento do agente de IA por meio de engenharia de prompt avançada, baseando as análises em padrões reconhecidos de mercado (como o OWASP ASVS).
* Implementação da funcionalidade de reescrever e exportar o documento original atualizado, contendo as novas seções de segurança integradas.
* Realização de testes dinâmicos e code review.

## 🤖 Ferramentas de IA Empregadas

Neste projeto, a Inteligência Artificial Generativa possui dois papéis fundamentais:
1. **No Produto (Core):** A IA é o motor principal da aplicação, atuando como o agente que analisa os requisitos de software e gera as recomendações de cibersegurança.
2. **No Desenvolvimento (Apoio):** Ferramentas de IA generativa (como ChatGPT, Gemini ou Copilot) serão utilizadas para auxiliar na escrita de algoritmos de extração de texto (parsers), estruturação de regex, e na lógica de orquestração do LangChain.

*(Nota: Os prompts mais relevantes utilizados durante o desenvolvimento de código serão registrados aqui em atualizações futuras, conforme diretriz da disciplina).*

## 🚀 Instruções para Execução Local
*(A ser preenchido durante a Fase 1 do desenvolvimento)*
