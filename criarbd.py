import sqlite3 as lite

con = lite.connect('dados.bd')

#Tabela de categorias
with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS Categorias (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT)")

    # Primary Key/ PK/ Chave primária = identificador de tabela, não podendo ser duplicado ou ter valor nulo - ex CPF - Dentro do banco de dados com linguagem SQL

#Tabela de receitas/ meu patrimonio
with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS Saldo_e_Investimentos (id INTEGER PRIMARY KEY AUTOINCREMENT, categoria TEXT, adicionado_em DATE, valor DECIMAL)")
    # Posteriormente trocar o valor de adicionado_em para data_de_entrada

#Tabela de gastos
with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS Gastos (id INTEGER PRIMARY KEY AUTOINCREMENT, categoria TEXT, retirado_em DATE, valor DECIMAL)")
    # Posteriormente trocar o valor de retirado_em para data_de_saida
