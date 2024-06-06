from tkinter import ttk, Frame, Entry, Button
from tkcalendar import Calendar, DateEntry
from datetime import date
import view
import sqlite3 as lite

global conexao_bd
conexao_bd = lite.connect('dados.bd')


def criar_aba3(notebook, bg_color):
    aba3 = Frame(notebook, bg=bg_color)
    notebook.add(aba3, text='Tabela de Receitas e Despesas')
    ttk.Label(aba3, text="Movimentação do seu dinheiro", font=("Arial", 24), background=bg_color).pack(pady=5)
     
    # Container para os espaços de adicionar
    container_adicionar = Frame(aba3, bg=bg_color)
    container_adicionar.pack(pady=20, side='top')
    
    # Espaço para adicionar receitas
    frame_receita = Frame(container_adicionar, bg=bg_color)
    frame_receita.pack(side='left')
    ttk.Label(frame_receita, text="Adicionar Receita", font=("Arial", 10), background=bg_color).pack(pady=10)
    
    ttk.Label(frame_receita, text="Data de Inclusão:", background=bg_color).pack()
    data_receita = DateEntry(frame_receita)
    data_receita.pack(pady=5)
    
    ttk.Label(frame_receita, text="Valor:", background=bg_color).pack()
    valor_receita = Entry(frame_receita)
    valor_receita.pack(pady=5)

    ttk.Label(frame_receita, text="Categoria:", background=bg_color).pack()
    categoria_receita = view.ver_categorias(conexao_bd, 'nome')
    categoria_receita = ttk.Combobox(frame_receita, values=categoria_receita)
    categoria_receita.pack(pady=5)
    
    Button(frame_receita, text="Adicionar Receita", command=lambda: view.inserir_receita(data_receita.get(), valor_receita.get(), categoria_receita.get())).pack(pady=10)
    
    # Espaço para adicionar despesas
    frame_despesa = Frame(container_adicionar, bg=bg_color)
    frame_despesa.pack(side='left', padx=10)  # Adiciona um espaço entre os frames de receita e despesa
    ttk.Label(frame_despesa, text="Adicionar Despesa", font=("Arial", 10), background=bg_color).pack(pady=10)
    
    ttk.Label(frame_despesa, text="Data de Inclusão:", background=bg_color).pack()
    data_despesa = DateEntry(frame_despesa)
    data_despesa.pack(pady=5)
    
    ttk.Label(frame_despesa, text="Valor:", background=bg_color).pack()
    valor_despesa = Entry(frame_despesa)
    valor_despesa.pack(pady=5)
    
    ttk.Label(frame_despesa, text="Categoria:", background=bg_color).pack()
    categorias_despesa = view.ver_categorias(conexao_bd, 'nome')
    categoria_despesa = ttk.Combobox(frame_despesa, values=categorias_despesa)
    categoria_despesa.pack(pady=5)
    
    Button(frame_despesa, text="Adicionar Despesa", command=lambda: view.inserir_despesa(data_despesa.get(), valor_despesa.get(), categoria_despesa.get())).pack(pady=10)

    # Espaço para adicionar Categoria
    frame_categoria = Frame(container_adicionar, bg=bg_color)
    frame_categoria.pack(pady=10, side='left')
    ttk.Label(frame_categoria, text="Adicionar Categoria", font=("Arial", 10), background=bg_color).pack(pady=10)
    
    ttk.Label(frame_categoria, text="Categoria:", background=bg_color).pack()
    valor_categoria = Entry(frame_categoria)
    valor_categoria.pack(pady=5, side='top')
    
    Button(frame_categoria, text="Adicionar Categoria", command=lambda: view.inserir_categoria(valor_categoria.get())).pack(pady=10, side='bottom', fill='y')

    # Container para tabelas
    container_tabelas = Frame(aba3, bg=bg_color)
    container_tabelas.pack(pady=10, after=container_adicionar)

    # Tabela de Receitas
    tabela_receitas = ttk.Treeview(container_tabelas)
    tabela_receitas['columns'] = ('Id', 'Categoria', 'Data', 'Valor')
    tabela_receitas.column('#0', width=0, stretch='NO')  # Oculta a primeira coluna (índices)
    tabela_receitas.column('Id', anchor='center', width=100)
    tabela_receitas.column('Categoria', anchor='center', width=100)
    tabela_receitas.column('Data', anchor='center', width=100)
    tabela_receitas.column('Valor', anchor='center', width=100)
    tabela_receitas.heading('Id', text='Id')
    tabela_receitas.heading('Categoria', text='Categoria')
    tabela_receitas.heading('Data', text='Data')
    tabela_receitas.heading('Valor', text='Valor')
    tabela_receitas.pack(pady=10, side='left', padx=5)
    
    
    # Exibir as receitas na tabela (substitua esta parte pelo código para obter as receitas do banco de dados)
    for receita in view.ver_Saldo_e_investimentos_full(conexao_bd):
        tabela_receitas.insert('', 'end', text='', values=(receita[0], receita[1], receita[2], receita[3]))

    # Tabela de Despesas
    tabela_receitas = ttk.Treeview(container_tabelas)
    tabela_receitas['columns'] = ('Id', 'Categoria', 'Data', 'Valor')
    tabela_receitas.column('#0', width=0, stretch='NO')  # Oculta a primeira coluna (índices)
    tabela_receitas.column('Id', anchor='center', width=100)
    tabela_receitas.column('Categoria', anchor='center', width=100)
    tabela_receitas.column('Data', anchor='center', width=100)
    tabela_receitas.column('Valor', anchor='center', width=100)
    tabela_receitas.heading('Id', text='Id')
    tabela_receitas.heading('Categoria', text='Categoria')
    tabela_receitas.heading('Data', text='Data')
    tabela_receitas.heading('Valor', text='Valor')
    tabela_receitas.pack(pady=10, side='left', padx=5)

    # Exibir as receitas na tabela (substitua esta parte pelo código para obter as receitas do banco de dados)
    for receita in view.ver_Gastos_full(conexao_bd):
        tabela_receitas.insert('', 'end', text='', values=(receita[0], receita[1], receita[2], receita[3]))  

    # Tabela de Despesas
    tabela_receitas = ttk.Treeview(container_tabelas)
    tabela_receitas['columns'] = ('Id', 'Categoria')
    tabela_receitas.column('#0', width=0, stretch='NO')  # Oculta a primeira coluna (índices)
    tabela_receitas.column('Id', anchor='center', width=100)
    tabela_receitas.column('Categoria', anchor='center', width=100)
    tabela_receitas.heading('Id', text='Id')
    tabela_receitas.heading('Categoria', text='Categoria')
    tabela_receitas.pack(pady=10, side='left', padx=5)

    # Exibir as receitas na tabela (substitua esta parte pelo código para obter as receitas do banco de dados)
    for receita in view.ver_categorias(conexao_bd, '*'):
        tabela_receitas.insert('', 'end', text='', values=(receita[0], receita[1]))     


    # Container para os espaços de excluir
    container_excluir = Frame(aba3, bg=bg_color)
    container_excluir.pack(pady=10, side='bottom')
    
    # Espaço para excluir receitas
    frame_excluir_receita = Frame(container_excluir, bg=bg_color)
    frame_excluir_receita.pack(pady=10, side='left', padx=20)
    ttk.Label(frame_excluir_receita, text="Excluir Receita", font=("Arial", 10), background=bg_color).pack(pady=10)
    
    ttk.Label(frame_excluir_receita, text="Receita:", background=bg_color).pack()
    categorias_excluir_receita = view.ver_Saldo_e_investimentos(conexao_bd)
    categoria_excluir_receita = ttk.Combobox(frame_excluir_receita, values=categorias_excluir_receita)
    categoria_excluir_receita.pack(pady=5)
    
    Button(frame_excluir_receita, text="Excluir Receita", command=lambda: view.deletar_Saldo_e_investimentos(categoria_excluir_receita.get())).pack(pady=10)
    
    # Espaço para excluir despesa   
    frame_excluir_despesa = Frame(container_excluir, bg=bg_color)
    frame_excluir_despesa.pack(pady=10, side='left', padx=20)
    ttk.Label(frame_excluir_despesa, text="Excluir Despesa", font=("Arial", 10), background=bg_color).pack(pady=10)
    
    ttk.Label(frame_excluir_despesa, text="Despesa:", background=bg_color).pack()
    categorias_excluir_categoria = view.ver_Gastos(conexao_bd)
    categoria_excluir_categoria = ttk.Combobox(frame_excluir_despesa, values=categorias_excluir_categoria)
    categoria_excluir_categoria.pack(pady=5)
    
    Button(frame_excluir_despesa, text="Excluir Despesa", command=lambda: view.deletar_Gastos(categoria_excluir_categoria.get())).pack(pady=10)
    
    # Espaço para excluir categoria
    frame_excluir_categoria = Frame(container_excluir, bg=bg_color)
    frame_excluir_categoria.pack(pady=10, side='left', padx=20)
    ttk.Label(frame_excluir_categoria, text="Excluir Categoria", font=("Arial", 10), background=bg_color).pack(pady=10)
    
    ttk.Label(frame_excluir_categoria, text="Categoria:", background=bg_color).pack()
    categorias_excluir_categoria = view.ver_categorias(conexao_bd, 'id')
    categoria_excluir_categoria = ttk.Combobox(frame_excluir_categoria, values=categorias_excluir_categoria)
    categoria_excluir_categoria.pack(pady=5)
    
    Button(frame_excluir_categoria, text="Excluir Categoria", command=lambda: view.deletar_categoria(categoria_excluir_categoria.get())).pack(pady=10)


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


