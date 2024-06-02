from tkinter import ttk, Frame, Entry, Button
from tkcalendar import Calendar, DateEntry
from datetime import date
import view 

def adicionar_categoria(categoria):
    # Lógica para adicionar receita ao banco de dados ou lista
    view.inserir_categoria(categoria)
    view.ver_categorias()
    print(f"Categoria adicionada: Valor: {categoria}")

def adicionar_receita(data, valor):
    # Lógica para adicionar receita ao banco de dados ou lista
    print(f"Receita adicionada: Data: {data}, Valor: {valor}")

def adicionar_despesa(data, valor, categoria):
    # Lógica para adicionar despesa ao banco de dados ou lista]
    view.deletar_categoria()
    print(f"Despesa adicionada: Data: {data}, Valor: {valor}, Categoria: {categoria}")

def obter_categorias():
    # Conectar ao banco de dados e obter as categorias
    categorias = view.ver_categorias
    return categorias

def criar_aba3(notebook, bg_color):
    aba3 = Frame(notebook, bg=bg_color)  # Usando Frame do Tkinter para suportar a configuração de cor de fundo
    notebook.add(aba3, text='Tabela de Receitas e Despesas')
    ttk.Label(aba3, text="Movimentação do seu dinheiro", font=("Arial", 24), background=bg_color).pack(pady=20)
    
    # Espaço para adicionar receitas
    frame_receita = Frame(aba3, bg=bg_color)
    frame_receita.pack(pady=20)
    ttk.Label(frame_receita, text="Adicionar Receita", font=("Arial", 18), background=bg_color).pack(pady=10)
    
    ttk.Label(frame_receita, text="Data de Inclusão:", background=bg_color).pack()
    data_receita = DateEntry(frame_receita)
    data_receita.pack(pady=5)
    
    ttk.Label(frame_receita, text="Valor:", background=bg_color).pack()
    valor_receita = Entry(frame_receita)
    valor_receita.pack(pady=5)
    
    Button(frame_receita, text="Adicionar Receita", command=lambda: adicionar_receita(data_receita.get(), valor_receita.get())).pack(pady=10)
    
    # Espaço para adicionar despesas
    frame_despesa = Frame(aba3, bg=bg_color)
    frame_despesa.pack(pady=20)
    ttk.Label(frame_despesa, text="Adicionar Despesa", font=("Arial", 18), background=bg_color).pack(pady=10)
    
    ttk.Label(frame_despesa, text="Data de Inclusão:", background=bg_color).pack()
    data_despesa = DateEntry(frame_despesa)
    data_despesa.pack(pady=5)
    
    ttk.Label(frame_despesa, text="Valor:", background=bg_color).pack()
    valor_despesa = Entry(frame_despesa)
    valor_despesa.pack(pady=5)
    
    ttk.Label(frame_despesa, text="Categoria:", background=bg_color).pack()
    categorias = obter_categorias()
    categoria_despesa = ttk.Combobox(frame_despesa, values=categorias)
    categoria_despesa.pack(pady=5)
    
    Button(frame_despesa, text="Adicionar Despesa", command=lambda: adicionar_despesa(data_despesa.get(), valor_despesa.get(), categoria_despesa.get())).pack(pady=10)

     # Espaço para adicionar Categoria
    frame_categoria = Frame(aba3, bg=bg_color)
    frame_categoria.pack(pady=20)
    ttk.Label(frame_categoria, text="Adicionar Categoria", font=("Arial", 18), background=bg_color).pack(pady=10)
    
   
    ttk.Label(frame_categoria, text="Categoria:", background=bg_color).pack()
    valor_categoria = Entry(frame_categoria)
    valor_categoria.pack(pady=5)
    
    Button(frame_categoria, text="Adicionar Categoria", command=lambda: adicionar_categoria(valor_categoria.get())).pack(pady=10)
    
    return aba3
# Criar Despesas 
    # inputar data, valor, e a categoria 
    # botão adiconar
#Criar Novas Recitas 
    # Inputar data, valor 
    # botão adicionar 
#Criar excluir ação 
    #botão de deletar 
#Criar Nova categoria 
    # botão adicionar categoria 


