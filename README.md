# Diário Pessoal Seguro

Sistema de diário pessoal desenvolvido em Python, com foco em autenticação segura de usuários através de hashing de senhas.

---

## Objetivo do Projeto

O objetivo deste projeto foi desenvolver uma aplicação de diário pessoal que armazenasse as entradas do usuário de forma segura, impedindo acesso não autorizado às informações. O desafio central era implementar um sistema de autenticação que seguisse boas práticas básicas de proteção de dados, evitando o armazenamento de senhas em texto puro — um erro comum em aplicações desenvolvidas sem foco em segurança.

---

## Tecnologias Utilizadas

- **Python** — linguagem principal do projeto
- **Programação Orientada a Objetos (OOP)** — estruturação do sistema em classes
- **Hashing SHA-256** — biblioteca `hashlib`, para criptografar senhas antes do armazenamento

---

## O que Foi Aprendido

Este projeto foi minha primeira aplicação prática de conceitos de segurança da informação em um sistema real. Os principais aprendizados foram:

- **Nunca armazenar senhas em texto puro**: entendi na prática por que isso é considerado uma falha crítica de segurança, e como o hashing resolve esse problema de forma simples e eficaz.
- **Diferença entre hashing e criptografia**: aprendi que hashing é uma via de mão única (não é possível "descriptografar" de volta), o que é exatamente o comportamento desejado para senhas.
- **Aplicação prática de OOP**: reforcei conceitos de classes e encapsulamento ao estruturar o sistema de autenticação como parte de uma arquitetura orientada a objetos.
- **Conexão com temas mais amplos**: o projeto me fez conectar prática de código com conceitos que estudei sobre LGPD e proteção de dados pessoais, entendendo que decisões técnicas pequenas têm implicações reais sobre a privacidade dos usuários.

---

## Como Executar

\```bash
python main.py
\```

O projeto está organizado em múltiplos arquivos:
- `main.py` — ponto de entrada da aplicação
- `diario.py` — lógica principal do sistema de diário e autenticação

---

## Contato

Desenvolvido por Gabriel — [GitHub](https://github.com/Gabriel03145)
```

**Atenção**: ao copiar, remova as barras invertidas (`\`) que coloquei antes de cada ` ``` ` na seção "Como Executar" — elas estão ali só porque, sem isso, esse bloco de código apareceria quebrado aqui no chat. No GitHub, sem as barras, fica assim:

```
```bash
python main.py
```
