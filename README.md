# Diário Pessoal Seguro

Sistema de diário pessoal desenvolvido em Python, com foco em controle de acesso por senha e boas práticas de encapsulamento em Programação Orientada a Objetos.

## Objetivo do Projeto

O objetivo deste projeto foi desenvolver uma aplicação de diário pessoal que restringisse o acesso às entradas do usuário através de um sistema de senha, aplicando conceitos de encapsulamento para proteger os dados internos da classe.

## Tecnologias Utilizadas

- **Python** — linguagem principal do projeto
- **Programação Orientada a Objetos (POO)** — estruturação do sistema em classes, com uso de atributos privados (name mangling)

## O que Foi Aprendido

- **Encapsulamento na prática**: usei atributos privados (com `__`) para impedir acesso direto às informações do diário e à senha armazenada na classe.
- **Controle de acesso por método**: implementei a verificação de senha dentro dos próprios métodos (`ler`, `trocar_senha`), usando `PermissionError` e `ValueError` para sinalizar tentativas inválidas.
- **Ponto de evolução identificado**: neste projeto a senha é comparada diretamente como texto, sem hashing — depois de estudar isso a fundo, apliquei hashing de senha (SHA-256) de forma mais robusta em um projeto posterior ([conta-bancaria](https://github.com/Gabriel03145/conta-bancaria)), que reflete melhor as boas práticas de segurança.

## Como Executar

```bash
python __main__.py
```

O projeto está organizado em múltiplos arquivos:

- `__main__.py` — ponto de entrada da aplicação
- `diario.py` — lógica principal do sistema de diário e controle de senha

## Contato

Desenvolvido por Gabriel — [GitHub](https://github.com/Gabriel03145)
