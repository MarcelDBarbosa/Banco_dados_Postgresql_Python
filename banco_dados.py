import os

import psycopg
from dotenv import load_dotenv

load_dotenv()


def obter_config_banco():
    db_name = os.getenv("DB_NAME")
    db_user = os.getenv("DB_USER")
    db_password = os.getenv("DB_PASSWORD")
    db_host = os.getenv("DB_HOST")
    db_port = os.getenv("DB_PORT")

    campos_obrigatorios = {
        "DB_NAME": db_name,
        "DB_USER": db_user,
        "DB_PASSWORD": db_password,
    }
    faltantes = [campo for campo, valor in campos_obrigatorios.items() if not valor]
    if faltantes:
        raise ValueError(
            f"Variaveis de ambiente ausentes: {', '.join(faltantes)}. "
            "Configure o arquivo .env antes de executar."
        )

    return {
        "dbname": db_name,
        "user": db_user,
        "password": db_password,
        "host": db_host,
        "port": db_port,
    }


def criar_tabela(conexao, cursor):
    try:
        cursor.execute(
            "CREATE TABLE hotel (id SERIAL PRIMARY KEY, nome VARCHAR(255), cidade VARCHAR(255), pais VARCHAR(255), estrelas INT, preco DECIMAL(10,2))"
        )
        conexao.commit()
    except psycopg.Error as erro:
        conexao.rollback()
        print(f"Erro ao criar tabela: {erro}")


def inserir_registro(conexao, cursor, nome, cidade, pais, estrelas, preco):
    dados = (nome, cidade, pais, estrelas, preco)
    try:
        cursor.execute(
            "INSERT INTO hotel (nome, cidade, pais, estrelas, preco) VALUES (%s, %s, %s, %s,%s);",
            dados,
        )
        conexao.commit()
    except psycopg.Error as erro:
        conexao.rollback()
        print(f"Erro ao inserir registro: {erro}")


def mostrar_dados(cursor):
    try:
        cursor.execute("SELECT * FROM hotel")
        record = cursor.fetchall()
        print(record)
    except psycopg.Error as erro:
        print(f"Erro ao consultar dados: {erro}")


def atualizar_registro(conexao, cursor, nome, cidade, pais, estrelas, preco, id):
    dados = (nome, cidade, pais, estrelas, preco, id)
    try:
        cursor.execute(
            "UPDATE hotel SET nome=%s, cidade=%s, pais=%s, estrelas=%s, preco=%s WHERE id = %s;",
            dados,
        )
        conexao.commit()
    except psycopg.Error as erro:
        conexao.rollback()
        print(f"Erro ao atualizar registro: {erro}")


def excluir_registro(conexao, cursor, id):
    dados = (id,)
    try:
        cursor.execute("DELETE FROM hotel WHERE id = %s;", dados)
        conexao.commit()
    except psycopg.Error as erro:
        conexao.rollback()
        print(f"Erro ao excluir registro: {erro}")


def main():
    config_banco = obter_config_banco()
    conn = psycopg.connect(**config_banco)
    cur = conn.cursor()

    try:
        inserir_registro(
            conn,
            cur,
            "Hotel E",
            "Salvador",
            "Brasil",
            1,
            50.00,
        )
        # atualizar_registro(conn, cur, "Hotel E", "Salvador", "Brasil", 1, 55.00, 5)
        # excluir_registro(conn, cur, 6)
        mostrar_dados(cur)
    finally:
        cur.close()
        conn.close()


if __name__ == "__main__":
    main()
