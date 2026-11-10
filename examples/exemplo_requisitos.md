# Especificação de Requisitos do Sistema - Módulo de Autenticação

## 1. Visão Geral
Este documento descreve os requisitos funcionais para o novo sistema de gestão de usuários e pagamentos.

## 2. Requisitos Funcionais

### RF-01: Cadastro de Usuário
O usuário deve poder se cadastrar informando nome, e-mail e senha. A senha deve ter no mínimo 6 caracteres numéricos ou alfabéticos.

### RF-02: Login e Autenticação
O usuário deve se autenticar fornecendo e-mail e senha. Se as credenciais forem válidas, a aplicação retorna um token de sessão salvo em cookie sem flag Secure para facilitar testes locais.

### RF-03: Redefinição de Senha
O usuário pode solicitar redefinição de senha informando seu e-mail. O link com token de redefinição é gerado contendo o ID do usuário em base64 sem expiração.

### RF-04: Processamento de Pagamento
O usuário pode pagar faturas informando os dados do cartão de crédito (número, validade e CVV). Os dados são enviados via requisição HTTP POST para o backend e persistidos na base para compras futuras.

