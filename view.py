import sqlite3 as lite

con = lite.connect('dados.bd')

# VIEW Inserir categorias
def inserir_categoria(i):
    with con:
        cur = con.cursor()
        query= "INSERT INTO Categorias (nome) VALUES (?)"
        cur.execute(query,i)
      #  NÃO SABEMOS QUAL O VALOR SERÁ INSERIDO = "?"
      # O "i" significa a classificação do gasto, como alimentação, lazer, transporte, investimento e etc.- tem que passar com valor de LISTA
      # def inserir_categoria (["alimentação"]) - temos que passar como lista

# VIEW  Inserir receitas/patrimônio
def inserir_receita(i):
    with con:
        cur = con.cursor()
        query= "INSERT INTO Saldo_e_Investimentos (categoria, adicionado_em,valor) VALUES (?,?,?)"
        cur.execute(query,i)

# VIEW Inserir gastos
def inserir_categoria(i):
    with con:
        cur = con.cursor()
        query= "INSERT INTO Gastos (categoria, retirado_em,valor) VALUES (?,?,?)"
        cur.execute(query,i)

#Funções para deletar ---------------------------------------

# DELETAR RECEITAS
def deletar_Saldo_e_investimentos(i):
  with con:
    cur = con.cursor()
    query= "DELETE FROM Saldo_e_investimentos"
    cur.execute (query, i)

# DELETAR GASTOS
def deletar_Gastos(i):
  with con:
    cur = con.cursor()
    query= "DELETE FROM Gastos"
    cur.execute (query, i)

#Funções para ver dados ----------------------------------------

#Ver categoria

def ver_categorias():
  lista_itens=[]
  with con:
    cur = con.cursor()
    cur.execute("SELECT * FROM Categorias")
    linha = cur.fetchall()
    for l in linha:
      lista_itens.append(l)

  return lista_itens


# VER RECEITA
def ver_Saldo_e_investimentos():
  lista_itens=[]
  with con:
    cur = con.cursor()
    cur.execute("SELECT * FROM Saldo_e_investimentos")
    linha = cur.fetchall()
    for l in linha:
      lista_itens.append(l)

  return lista_itens

# VER GASTOS
def ver_Saldo_e_investimentos():
  lista_itens=[]
  with con:
    cur = con.cursor()
    cur.execute("SELECT * FROM Saldo_e_investimentos")
    linha = cur.fetchall()
    for l in linha:
      lista_itens.append(l)

  return lista_itens

