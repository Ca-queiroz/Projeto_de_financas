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
def inserir_gastos(i):
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
def ver_Gastos():
  lista_itens=[]
  with con:
    cur = con.cursor()
    cur.execute("SELECT * FROM Saldo_e_investimentos")
    linha = cur.fetchall()
    for l in linha:
      lista_itens.append(l)

  return lista_itens

def tabela():
    gastos = ver_gastos()
    receitas = ver_Receitas()

    tabela_lista = []

    for i in gastos:
        tabela_lista.append(i)

    for i in receitas:
        tabela_lista.append(i)

    return tabela_lista

def bar_valores():
    # Receita Total ------------------------
    receitas = ver_Receitas()
    receitas_lista = []

    for i in receitas:
        receitas_lista.append(i[3])

    receita_total = sum(receitas_lista)

    # Despesas Total ------------------------
    receitas = ver_gastos()
    despesas_lista = []

    for i in receitas:
        despesas_lista.append(i[3])

    despesas_total = sum(despesas_lista)

    # Despesas Total ------------------------
    saldo_total = receita_total - despesas_total

    return[receita_total,despesas_total,saldo_total]

def percentagem_valor():

    # Receita Total ------------------------
    receitas = ver_Receitas()
    receitas_lista = []

    for i in receitas:
        receitas_lista.append(i[3])

    receita_total = sum(receitas_lista)

    # Despesas Total ------------------------
    receitas = ver_gastos()
    despesas_lista = []

    for i in receitas:
        despesas_lista.append(i[3])

    despesas_total = sum(despesas_lista)

    # Despesas Total ------------------------
    total =  ((receita_total - despesas_total) / receita_total) * 100

    return[total]


def pie_valores():
    gastos = ver_gastos()
    tabela_lista = []

    for i in gastos:
        tabela_lista.append(i)

    dataframe = pd.DataFrame(tabela_lista,columns = ['id', 'Categoria', 'Data', 'valor'])

    # Get the sum of the durations per month
    dataframe = dataframe.groupby('Categoria')['valor'].sum()
   
    lista_quantias = dataframe.values.tolist()
    lista_categorias = []

    for i in dataframe.index:
        lista_categorias.append(i)

    return([lista_categorias,lista_quantias])
