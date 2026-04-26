[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/) ![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)

# Sistema de Cadastro de Hoteis com PostgreSQL

Este script (`banco_dados.py`) demonstra operacoes basicas de banco de dados com Python:

- criacao de tabela;
- insercao de registros;
- consulta de dados;
- atualizacao de registros;
- exclusao de registros.

As operacoes SQL usam consultas parametrizadas (`%s`), o que ajuda a prevenir SQL Injection.

## Requisito obrigatorio

E necessario ter o **PostgreSQL instalado localmente** e em execucao para que o script funcione.

## Dependencias

As dependencias estao no arquivo `requirements.txt`:

- `psycopg==3.3.3`
- `python-dotenv==1.0.1`

## Setup do ambiente

1. Acesse a pasta do projeto:

```bash
cd LocalEscolhido
```

2. (Opcional, recomendado) Crie e ative um ambiente virtual:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. Instale as dependencias:

```bash
pip install -r requirements.txt
```

4. Crie o arquivo `.env` na pasta `LocalEscolhido` com as variaveis:

```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=viagens
DB_USER=seu_usuario
DB_PASSWORD=sua_senha
```

## Preparacao do banco

Antes de executar o script, garanta que:

- o servidor PostgreSQL local esta ativo;
- o banco informado em `DB_NAME` existe;
- o usuario informado tem permissao para criar tabela e manipular dados.

## Execucao

Rode o script:

```bash
python banco_dados.py
```

## Observacoes importantes

- Se quiser criar a tabela pelo script, chame a funcao `criar_tabela(conn, cur)` antes das operacoes de insercao.
- Em caso de erro de SQL, o script faz `rollback` para evitar transacoes quebradas.
- Nao versionar o arquivo `.env` com credenciais reais.
