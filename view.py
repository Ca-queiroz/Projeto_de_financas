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
<<<<<<< HEAD
def inserir_gastos(i):
=======
def inserir_despesa(retirado_em, valor, categoria):
>>>>>>> 0a028ad2d93844bce2e64a34af52104afae819c7
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

# Ver receita sumarizada
def ver_Saldo_e_investimentos_sum(conexao_bd):
  cur = conexao_bd.cursor()
  cur.execute("SELECT sum(valor) FROM Saldo_e_investimentos")
  receita_sum = cur.fetchall()
  return receita_sum[0][0]
 

# VER GASTOS
<<<<<<< HEAD
def ver_Gastos():
=======
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

def ver_Gastos_sum(conexao_bd):
  cur = conexao_bd.cursor()
  cur.execute("SELECT sum(valor) FROM Gastos")
  despesa_sum = cur.fetchall()
  return despesa_sum[0][0]

def ver_gastos_agrupados_por_categoria(conexao_bd):
  cur = conexao_bd.cursor()
  cur.execute("SELECT categoria, sum(valor) as valor FROM Gastos group by categoria")
  despesa_sum_group_by = cur.fetchall()
  return despesa_sum_group_by  


def ver_Gastos_2():
>>>>>>> 0a028ad2d93844bce2e64a34af52104afae819c7
  lista_itens=[]
  with con:
    cur = con.cursor()
    cur.execute("SELECT * FROM Saldo_e_investimentos")
    linha = cur.fetchall()
    for l in linha:
<<<<<<< HEAD
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
=======
      lista_itens.append(l)  
>>>>>>> 0a028ad2d93844bce2e64a34af52104afae819c7
