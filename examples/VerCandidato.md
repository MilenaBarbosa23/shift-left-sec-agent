# Documento de Requisitos de Software — Triagem de Candidatos (Ver Candidato)

**Projeto:** WeGrano — Conexão no Agronegócio Cafeeiro  
**Módulo:** Gestão de Candidaturas e Seleção de Trabalhadores (Visão do Produtor)  
**Documento:** `VerCandidato.md`  
**Versão:** 1.0  
**Data:** 07 de Novembro de 2026  
**Status:** Especificação Oficial  

---

## 1. Visão Geral

Este documento especifica os **Requisitos Funcionais (RF)**, **Regras de Negócio (RN)** e **Requisitos Não Funcionais de Segurança e Desempenho (RNF)** da tela de **Triagem de Candidatos (Ver Candidato)**.

Acessada a partir do botão **"Ver Interessados"** presente nos cards de vagas em *Minhas Vagas*, esta tela é o ambiente onde o Produtor Rural gerencia, avalia e toma decisões sobre todos os trabalhadores que se candidataram às suas oportunidades de colheita e tratos culturais. 

O produtor conta com uma visão contextualizada da vaga anunciada no topo da página e uma grade interativa de candidatos, podendo:
1. Analisar o resumo profissional, histórico de safras, avaliação média e necessidades logísticas (como necessidade de alojamento).
2. Acessar o perfil profissional completo com um clique na foto ou no botão **"Ver Perfil"**.
3. **Aceitar** ou **Rejeitar** candidaturas de forma ágil para fechar suas turmas de safra.
4. **Entrar em contato direto por telefone/WhatsApp** com mensagem pré-formatada para acelerar a contratação.

---

## 2. Requisitos Funcionais (RF)

---

### RF-VC01 — Painel de Contexto da Vaga no Topo da Página
- **Descrição:** Como Produtor, quero visualizar no topo da tela as informações principais da vaga selecionada para manter total orientação sobre qual oportunidade e período estou avaliando.
- **Critérios de Aceite:**
  1. **Cabeçalho de Identificação:**
     - Título principal da página: **"Triagem de Candidatos"**.
     - Subtítulo orientativo: *"Avalie trabalhadores rurais e feche suas turmas para a colheita"*.
     - Botão de navegação: *"← Voltar para Minhas Vagas"*.
  2. **Card de Resumo Operacional da Vaga:**
     - **Título da Vaga:** Nome do cargo/função (ex.: *Colheita Manual de Café Arábica*).
     - **Nome da Fazenda e Local:** Propriedade e município (ex.: *Fazenda Santa Maria — Patrocínio, MG*).
     - **Período de Execução:** Data de início e término da atividade (ex.: *"15/11/2026 até 15/01/2027"* ou *"Início em 15/11/2026 (Contínuo)"*).
     - **Badge de Status Operacional:** Tag destacando o status da vaga (`Ativa`, `Inativa` ou `Concluída`).
     - **Métricas Rápidas:**
       - Total de inscritos na vaga (ex.: *14 candidatos*).
       - Candidatos aceitos / Vagas preenchidas (ex.: *5 contratados de 10 vagas*).
       - Candidatos pendentes de avaliação (ex.: *9 aguardando resposta*).

---

### RF-VC02 — Grade de Cards de Candidatos Inscritos
- **Descrição:** Como Produtor, quero visualizar os trabalhadores inscritos na vaga em cards individuais bem organizados para comparar experiências e perfis com facilidade.
- **Critérios de Aceite:**
  1. Cada card de candidato deve conter, de forma padronizada e legível:
     - **Foto de Perfil do Trabalhador:** Imagem circular de identificação (com avatar padrão com as iniciais caso não tenha foto customizada).
     - **Nome Completo do Trabalhador:** Em destaque (ex.: *Marcos Antônio Pereira*).
     - **Média de Avaliação (Estrelas):** Nota numérica formatada com 1 casa decimal acompanhada de ícone de estrela dourada (ex.: ★ **4.8**).
     - **Experiência na Cafeicultura / Tempo de Lida:** Destaque para o histórico prático em safras (ex.: *8 safras no Cerrado Mineiro*).
     - **Cidade / Origem de Residência:** Município e UF de onde o trabalhador reside (ex.: *Patrocínio - MG*).
     - **Vaga Vinculada:** Identificação da vaga pretendida (ex.: *Vaga: Colheita Manual de Café Arábica*).
     - **Badge de Necessidades Logísticas Especiais:** Tag visual com destaque de cor de alerta suave caso o candidato possua necessidades logísticas declaradas:
       - 🏠 `Necessita Alojamento`
       - 🚌 `Necessita Transporte Rural`
       - 👥 `Candidatura em Grupo / Turma Familiar`
     - **Habilidades em Destaque:** Até 3 principais tags de habilidades cadastradas pelo trabalhador (ex.: *Colheita Manual*, *Derriça Costal*, *Terreiro*).
     - **Data do Envio da Candidatura:** Data e hora em que a inscrição foi realizada (ex.: *"Inscrito há 2 dias"*).
     - **Badge de Status da Candidatura:**
       - `Pendente` (Amarelo: aguardando decisão).
       - `Aceito` (Verde: aprovado pelo produtor).
       - `Recusado` (Cinza/Vermelho: não selecionado).

---

### RF-VC03 — Abertura do Perfil Completo do Trabalhador (Foto e Botão)
- **Descrição:** Como Produtor, quero poder ver o perfil detalhado do trabalhador tanto ao clicar sobre a foto de perfil quanto ao apertar um botão dedicado "Ver Perfil".
- **Critérios de Aceite:**
  1. **Clique na Foto de Perfil:**
     - A foto de perfil do trabalhador no card deve ser um elemento interativo clicável, com cursor pointer (`cursor: pointer`), leve efeito de hover (zoom/brilho suave) e tooltip: *"Ver perfil completo de [Nome]"*.
  2. **Botão Explícito "Ver Perfil":**
     - O card deve conter um botão secundário claramente rotulado como **"Ver Perfil"** ou **"Perfil Completo"** (com ícone de identificação/usuário).
  3. **Comportamento de Visualização:**
     - Ao clicar na foto ou no botão "Ver Perfil", o sistema abre o perfil completo do trabalhador (em modal expansivo de alta performance ou redirecionando para a rota `/produtor/trabalhadores/{id}`).
     - O perfil completo exibe a biografia profissional, histórico completo de avaliações de outros produtores da região, lista detalhada de habilidades comprovadas, contatos e cidades onde já trabalhou em safras anteriores.

---

### RF-VC04 — Ação de Aceitar Candidato
- **Descrição:** Como Produtor, quero aprovar o candidato para garantir sua vaga na minha turma de colheita.
- **Critérios de Aceite:**
  1. O card deve possuir um botão de ação com estilo positivo: **"Aceitar Candidato"** ou **"Aprovar"** (estilo verde com ícone de check `✓`).
  2. Ao acionar o botão:
     - O sistema exibe um diálogo breve de confirmação:  
       *"Deseja aprovar a candidatura de **[Nome do Trabalhador]** para a vaga **[Título da Vaga]**?"*.
     - Ao confirmar, o status da candidatura é atualizado para `Aceito`.
     - O contador de vagas preenchidas no painel de contexto da vaga é incrementado em tempo real.
     - Uma notificação no sistema (push/alerta interno) é gerada para o trabalhador informando que sua candidatura foi aceita.
     - O card do candidato é atualizado visualmente, destacando o selo verde de aprovação.

---

### RF-VC05 — Ação de Recusar / Rejeitar Candidato
- **Descrição:** Como Produtor, quero rejeitar candidatos cujo perfil não atenda às necessidades operacionais da vaga para manter a listagem organizada.
- **Critérios de Aceite:**
  1. O card deve possuir um botão de ação secundário: **"Rejeitar"** ou **"Recusar"** (estilo neutro ou vermelho suave com ícone de `✕`).
  2. Ao acionar o botão:
     - O sistema exibe um diálogo de confirmação:  
       *"Tem certeza de que deseja recusar este candidato?"* com opção opcional de informar motivo interno (ex.: *Turma completa*, *Falta de experiência necessária*, *Logística inviável*).
     - Ao confirmar, o status da candidatura passa para `Recusado`.
     - O trabalhador recebe atualização discreta no seu painel de vagas inscritas com status de processo encerrado.

---

### RF-VC06 — Contato Direto por Telefone e WhatsApp Integrado
- **Descrição:** Como Produtor, quero um botão direto para ligar ou conversar com o trabalhador via WhatsApp para alinhar detalhes de chegada na fazenda, transporte e alojamento.
- **Critérios de Aceite:**
  1. O card deve disponibilizar um botão de destaque com o ícone oficial do WhatsApp: **"Conversar no WhatsApp"** (ou ícone de telefone/WhatsApp ao lado das ações).
  2. **Comportamento do Clique (Redirecionamento Direto):**
     - O link deve gerar a URI oficial com protocolo universal:  
       `https://wa.me/55{DDD}{TELEFONE}?text={MENSAGEM_CODIFICADA}`.
     - **Mensagem Pré-configurada Inteligente:**  
       O texto padrão enviado já carrega os dados de contexto para evitar digitação manual:  
       *"Olá [Nome do Trabalhador], aqui é o produtor da [Nome da Fazenda]. Vi sua inscrição no WeGrano para a vaga de [Título da Vaga] e gostaria de conversar sobre a contratação."*
     - No desktop, o clique abre o WhatsApp Web em nova aba (`target="_blank"`).
     - No celular/dispositivo móvel, o clique abre diretamente o aplicativo nativo do WhatsApp.
  3. **Visualização do Telefone:**
     - Exibição do número no formato brasileiro padronizado: `(XX) XXXXX-XXXX`.
     - Suporte a link nativo `tel:+55XXXXXXXXXXX` caso o produtor prefira realizar uma ligação telefônica comum diretamente do smartphone.

---

### RF-VC07 — Sistema de Filtros e Busca Rápida na Triagem
- **Descrição:** Como Produtor, quero filtrar a lista de interessados para encontrar perfis específicos ou gerenciar quem ainda não foi avaliado.
- **Critérios de Aceite:**
  1. **Filtro por Status da Candidatura:**
     - Tabs ou seletores rápidos:
       - `Todos os Inscritos` (com contagem total)
       - `Pendentes` (padrão)
       - `Aceitos` (turma confirmada)
       - `Recusados`
  2. **Filtro Rápido por Necessidade de Alojamento:**
     - Checkbox/Chip: `[X] Apenas candidatos que necessitam alojamento` ou `[X] Apenas candidatos com condução própria`.
  3. **Campo de Busca:**
     - Campo de busca por texto com debounce (300ms) para pesquisar por nome do trabalhador ou cidade de origem.
  4. **Ordenação:**
     - Dropdown de ordenação:
       - *Mais recentes primeiro (Data de inscrição DESC)*
       - *Melhor avaliação primeiro (Nota das estrelas DESC)*
       - *Mais safras de experiência primeiro (Anos de experiência DESC)*

---

### RF-VC08 — Tratamento de Lista Vazia (Empty States)
- **Descrição:** Como Produtor, quero receber orientações claras caso a vaga ainda não possua interessados inscritos ou se nenhum resultado corresponder aos filtros.
- **Critérios de Aceite:**
  1. **Nenhum inscrito na vaga ainda:**
     - Ilustração temática com texto: *"Nenhum trabalhador se inscreveu nesta vaga até o momento."*
     - Dica útil: *"Dica WeGrano: Vagas com valores claros e benefícios detalhados (como almoço e transporte) recebem até 3x mais candidaturas."*
     - Botão: *"Compartilhar Anúncio da Vaga"* (copia link direto de divulgação).
  2. **Filtro sem resultados:**
     - Mensagem: *"Nenhum candidato corresponde aos filtros selecionados."* com botão *"Limpar Filtros"*.

---

## 3. Requisitos Não Funcionais de Segurança e Desempenho (RNF)

---

### RNF-SEG-01 — Controle de Acesso e Prevenção de IDOR/BOLA (OWASP A01)
- **Descrição:** Um produtor não pode ter acesso à triagem de candidatos de vagas pertencentes a outros produtores rurais.
- **Diretrizes Técnicas:**
  - O endpoint `GET /api/vagas/{vagaId}/candidaturas` deve checar no back-end se o `vaga.produtor_id` é idêntico ao `authenticatedUserId` contido no token JWT.
  - Caso haja divergência, a requisição é negada com código `403 Forbidden` e evento registrado no log de segurança.

---

### RNF-SEG-02 — Proteção de Dados Pessoais do Trabalhador (LGPD)
- **Descrição:** Resguardar o número de telefone e dados de contato dos trabalhadores rurais contra raspagem automatizada (web scraping) e vazamentos.
- **Diretrizes Técnicas:**
  - O telefone completo do candidato só é disponibilizado via API se o produtor estiver devidamente logado e for o proprietário comprovado da vaga para a qual o trabalhador se candidatou voluntariamente.
  - O endpoint de listagem de candidaturas deve implementar limitação de taxa (Rate Limiting) de no máximo 60 requisições por minuto por produtor.
  - Não expor números de CPF ou documentos civis na listagem de triagem.

---

### RNF-SEG-03 — Idempotência e Auditoria nas Transições de Status
- **Descrição:** Evitar aprovações duplas ou inconsistência na contagem de turmas ao aceitar candidatos.
- **Diretrizes Técnicas:**
  - Os endpoints de alteração de status (`POST /api/candidaturas/{id}/aceitar` e `POST /api/candidaturas/{id}/rejeitar`) devem ser idempotentes.
  - Registro de auditoria: `id_candidatura`, `id_vaga`, `id_produtor`, `id_trabalhador`, `status_anterior`, `novo_status` e `timestamp`.

---

### RNF-PERF-01 — Paginação e Carregamento Rápido dos Cards
- **Descrição:** Vagas populares com centenas de inscritos devem carregar instantaneamente sem degradação de performance no front-end.
- **Diretrizes Técnicas:**
  - Implementação de paginação paginada no back-end via Spring Data JPA (`page`, `size = 10` ou `15` cards por página).
  - Fotos de perfil devem ser carregadas com `loading="lazy"` e miniaturas compactadas geradas no upload (thumbnails de 150x150px).

---

## 4. Matriz de Componentes do Card do Candidato

| Elemento Visual | Origem do Dado / Exemplo Real | Comportamento / Regra |
|:---|:---|:---|
| **Foto do Candidato** | Foto de perfil do trabalhador | Clicável; abre o perfil completo do trabalhador |
| **Nome do Trabalhador** | *Marcos Antônio Pereira* | Título em destaque do card |
| **Avaliação** | ★ **4.8** (12 avaliações) | Média calculada de safras anteriores com produtores da região |
| **Experiência** | *8 safras no Cerrado Mineiro* | Tempo de vivência prática declarado e verificado na cafeicultura |
| **Localização** | *Patrocínio - MG* | Cidade e estado onde o trabalhador reside atualmente |
| **Vaga Alvo** | *Vaga: Colheita Manual de Café Arábica* | Confirmação da oportunidade para a qual ele se inscreveu |
| **Alerta Logístico** | 🏠 `Necessita Alojamento` | Badge chamativo para planejamento de estrutura da fazenda |
| **Habilidades** | *Colheita Manual*, *Derriça Costal* | Chips com competências operacionais relevantes |
| **Botão "Ver Perfil"** | Ação secundária | Abre modal ou página com biografia e histórico profissional completo |
| **Botão "Conversar no WhatsApp"** | Telefone formatado: `(34) 99876-5432` | Abre o WhatsApp com mensagem contextualizada da vaga pronta para envio |
| **Botão "Aceitar"** | Ação positiva (`✓ Aceitar`) | Aprova a candidatura, incrementa a turma e notifica o trabalhador |
| **Botão "Rejeitar"** | Ação neutra/destrutiva (`✕ Rejeitar`) | Recusa a candidatura mediante confirmação |

