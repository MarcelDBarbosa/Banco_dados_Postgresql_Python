[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/) ![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)

# Sistema de Cadastro de Hoteis com PostgreSQL

Este script (`banco_dados.py`) demonstra operações básicas de banco de dados com Python:

- criação de tabela;
- inserção de registros;
- consulta de dados;
- atualização de registros;
- exclusão de registros.

As operações SQL usam consultas parametrizadas (`%s`), o que ajuda a prevenir SQL Injection.

## Requisito obrigatório

É necessário ter o **PostgreSQL instalado localmente** e em execução para que o script funcione.

## Dependências

As dependências estão no arquivo `requirements.txt`:

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

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Crie o arquivo `.env` na pasta `LocalEscolhido` com as variáveis:

```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=viagens
DB_USER=seu_usuario
DB_PASSWORD=sua_senha
```

## Preparação do banco

Antes de executar o script, garanta que:

- o servidor PostgreSQL local está ativo;
- o banco informado em `DB_NAME` existe;
- o usuário informado tem permissão para criar tabela e manipular dados.

## Execução

Rode o script:

```bash
python banco_dados.py
```

## Observações importantes

- Se quiser criar a tabela pelo script, chame a função `criar_tabela(conn, cur)` antes das operações de inserção.
- Em caso de erro de SQL, o script faz `rollback` para evitar transações quebradas.
- Não versionar o arquivo `.env` com credenciais reais.
