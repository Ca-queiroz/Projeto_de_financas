import sqlite3 as lite

con = lite.connect('dados.bd')

# VIEW Inserir categorias
def inserir_categoria(nome_categoria):
    with con:
        cur = con.cursor()
        cur.execute("INSERT INTO Categorias (nome) VALUES (?)", (nome_categoria,))
        con.commit()
      #  NÃO SABEMOS QUAL O VALOR SERÁ INSERIDO = "?"
      # O "i" significa a classificação do gasto, como alimentação, lazer, transporte, investimento e etc.- tem que passar com valor de LISTA
      # def inserir_categoria (["alimentação"]) - temos que passar como lista

# VIEW  Inserir receitas/patrimônio
def inserir_receita(adicionado_em, valor, categoria):
    with con:
        cur = con.cursor()
        cur.execute("INSERT INTO Saldo_e_Investimentos (adicionado_em, valor, categoria) VALUES (?,?,?)", (adicionado_em, valor, categoria,))
        con.commit()

# VIEW Inserir gastos
def inserir_despesa(retirado_em, valor, categoria):
    with con:
        cur = con.cursor()
        cur.execute("INSERT INTO Gastos (retirado_em, valor, categoria) VALUES (?,?,?)", (retirado_em, valor, categoria,))
        con.commit()

#Funções para deletar ---------------------------------------

# DELETAR RECEITAS
def deletar_Saldo_e_investimentos(receita_excluida):
  with con:
    cur = con.cursor()
    cur.execute("DELETE FROM Saldo_e_investimentos where id = ?", (receita_excluida,))
    con.commit()

# DELETAR GASTOS
def deletar_Gastos(despesa_excluida):
  with con:
    cur = con.cursor()
    cur.execute("DELETE FROM Gastos where id = ?", (despesa_excluida,))
    con.commit()

# DELETAR GASTOS
def deletar_categoria(categoria_excluida):
  with con:
    cur = con.cursor()
    cur.execute("DELETE FROM categorias where id = ?", (categoria_excluida,))
    con.commit()
    

#Funções para ver dados ----------------------------------------

#Ver categoria

def ver_categorias(conexao_bd, campo):
  cur = conexao_bd.cursor()
  cur.execute(f'SELECT {campo} FROM Categorias')
  categorias = cur.fetchall()
  return categorias

def ver_categorias_full(conexao_bd):
  cur = conexao_bd.cursor()
  cur.execute('SELECT * FROM Categorias')
  categorias = cur.fetchall()
  return categorias


# VER RECEITA
def ver_Saldo_e_investimentos(conexao_bd):
  cur = conexao_bd.cursor()
  cur.execute("SELECT id FROM Saldo_e_investimentos")
  receita = cur.fetchall()
  return receita

# VER RECEITA
def ver_Saldo_e_investimentos_full(conexao_bd):
  cur = conexao_bd.cursor()
  cur.execute("SELECT * FROM Saldo_e_investimentos")
  receita = cur.fetchall()
  return receita

# VER GASTOS
def ver_Gastos(conexao_bd):
  cur = conexao_bd.cursor()
  cur.execute("SELECT id FROM Gastos")
  despesa = cur.fetchall()
  return despesa

# VER GASTOS
def ver_Gastos_full(conexao_bd):
  cur = conexao_bd.cursor()
  cur.execute("SELECT * FROM Gastos")
  despesa = cur.fetchall()
  return despesa


