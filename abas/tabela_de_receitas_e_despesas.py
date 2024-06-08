from PIL import Image, ImageTk
from tkinter import PhotoImage
import tkinter as tk
from tkinter import Tk, ttk, Frame, Entry, Button, messagebox
from tkcalendar import Calendar, DateEntry
from datetime import date
import view as view 
import sqlite3 as lite

global conexao_bd
conexao_bd = lite.connect('dados.bd')
# Carregando as imagens para as abas
# imagem1 = Image.open("abas/images/fluxodeinançasimg.png")
# imagem1 = ImageTk.PhotoImage(imagem1)

def criar_aba3(notebook, bg_color):
    while True:
        aba3 = Frame(notebook, bg=bg_color)
        notebook.add(aba3, text='Tabela de Receitas e Despesas')
        Framecima = Frame(aba3, width=1280, height=150, relief="flat")
        Framecima.pack(side='top', fill='both')
        imagem1 = Image.open("abas/images/receitaedespesasimg.png")
        imagem1 = ImageTk.PhotoImage(imagem1)
        label_imagem1 = tk.Label(Framecima, image=imagem1)
        label_imagem1.image = imagem1  # Garante que a imagem não seja apagada pela coleta de lixo
        label_imagem1.pack()

        # Container para os espaços de adicionar
        container_adicionar = Frame(aba3, bg=bg_color)
        container_adicionar.pack(pady=20, side='top')
        
        # Espaço para adicionar receitas
        frame_receita = Frame(container_adicionar, bg=bg_color)
        frame_receita.pack(side='left')
        ttk.Label(frame_receita, text="Adicionar Receita", font=("Helvetica", 10), background=bg_color).pack(pady=10)
        
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
        
        Button(frame_receita, text="Adicionar Receita", command=lambda: adicionar_receita(data_receita.get(), valor_receita.get(), categoria_receita.get())).pack(pady=10)
        
        # Espaço para adicionar despesas
        frame_despesa = Frame(container_adicionar, bg=bg_color)
        frame_despesa.pack(side='left', padx=10)  # Adiciona um espaço entre os frames de receita e despesa
        ttk.Label(frame_despesa, text="Adicionar Despesa", font=("Helvetica", 10), background=bg_color).pack(pady=10)
        
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
        
        Button(frame_despesa, text="Adicionar Despesa", command=lambda: adicionar_despesa(data_despesa.get(), valor_despesa.get(), categoria_despesa.get())).pack(pady=10)

        # Espaço para adicionar Categoria
        frame_categoria = Frame(container_adicionar, bg=bg_color)
        frame_categoria.pack(pady=10, side='left')
        ttk.Label(frame_categoria, text="Adicionar Categoria", font=("Helvetica", 10), background=bg_color).pack(pady=10)
        
        ttk.Label(frame_categoria, text="Categoria:", background=bg_color).pack()
        valor_categoria = Entry(frame_categoria)
        valor_categoria.pack(pady=5, side='top')
        
        Button(frame_categoria, text="Adicionar Categoria", command=lambda: adicionar_categoria(valor_categoria.get())).pack(pady=10, side='bottom', fill='y')
        
        # Container para tabelas
        container_tabelas = Frame(aba3, bg=bg_color)
        container_tabelas.pack(pady=10, after=container_adicionar)

        # Tabela de Receitas
        global tabela_receitas
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

        for receita in view.ver_Saldo_e_investimentos_full(conexao_bd):
            tabela_receitas.insert('', 'end', text='', values=(receita[0], receita[1], receita[2], receita[3]))   
    
        # Tabela de Despesas
        global tabela_despesas
        tabela_despesas = ttk.Treeview(container_tabelas)
        tabela_despesas['columns'] = ('Id', 'Categoria', 'Data', 'Valor')
        tabela_despesas.column('#0', width=0, stretch='NO')  # Oculta a primeira coluna (índices)
        tabela_despesas.column('Id', anchor='center', width=100)
        tabela_despesas.column('Categoria', anchor='center', width=100)
        tabela_despesas.column('Data', anchor='center', width=100)
        tabela_despesas.column('Valor', anchor='center', width=100)
        tabela_despesas.heading('Id', text='Id')
        tabela_despesas.heading('Categoria', text='Categoria')
        tabela_despesas.heading('Data', text='Data')
        tabela_despesas.heading('Valor', text='Valor')
        tabela_despesas.pack(pady=10, side='left', padx=5)

        # Exibir as receitas na tabela (substitua esta parte pelo código para obter as receitas do banco de dados)
        for despesa in view.ver_Gastos_full(conexao_bd):
            tabela_despesas.insert('', 'end', text='', values=(despesa[0], despesa[1], despesa[2], despesa[3])) 

        # Tabela de Categorias
        global tabela_categorias
        tabela_categorias = ttk.Treeview(container_tabelas)
        tabela_categorias['columns'] = ('Id', 'Categoria')
        tabela_categorias.column('#0', width=0, stretch='NO')  # Oculta a primeira coluna (índices)
        tabela_categorias.column('Id', anchor='center', width=100)
        tabela_categorias.column('Categoria', anchor='center', width=100)
        tabela_categorias.heading('Id', text='Id')
        tabela_categorias.heading('Categoria', text='Categoria')
        tabela_categorias.pack(pady=10, side='left', padx=5)

        # Exibir as despesas na tabela (substitua esta parte pelo código para obter as despesas do banco de dados)
        for categoria in view.ver_categorias(conexao_bd, '*'):
            tabela_categorias.insert('', 'end', text='', values=(categoria[0], categoria[1]))     


        # Container para os espaços de excluir
        container_excluir = Frame(aba3, bg=bg_color)
        container_excluir.pack(pady=10, side='bottom')
        
        # Espaço para excluir receitas
        frame_excluir_receita = Frame(container_excluir, bg=bg_color)
        frame_excluir_receita.pack(pady=10, side='left', padx=20)
        ttk.Label(frame_excluir_receita, text="Excluir Receita", font=("Helvetica", 10), background=bg_color).pack(pady=10)
        
        ttk.Label(frame_excluir_receita, text="Receita:", background=bg_color).pack()
        categorias_excluir_receita = view.ver_Saldo_e_investimentos(conexao_bd)
        categoria_excluir_receita = ttk.Combobox(frame_excluir_receita, values=categorias_excluir_receita)
        categoria_excluir_receita.pack(pady=5)
        
        Button(frame_excluir_receita, text="Excluir Receita", command=lambda: excluir_receita(categoria_excluir_receita.get())).pack(pady=10)
        
        # Espaço para excluir despesa   
        frame_excluir_despesa = Frame(container_excluir, bg=bg_color)
        frame_excluir_despesa.pack(pady=10, side='left', padx=20)
        ttk.Label(frame_excluir_despesa, text="Excluir Despesa", font=("Helvetica", 10), background=bg_color).pack(pady=10)
        
        ttk.Label(frame_excluir_despesa, text="Despesa:", background=bg_color).pack()
        categorias_excluir_despesa = view.ver_Gastos(conexao_bd)
        categoria_excluir_despesa = ttk.Combobox(frame_excluir_despesa, values=categorias_excluir_despesa)
        categoria_excluir_despesa.pack(pady=5)
        
        Button(frame_excluir_despesa, text="Excluir Despesa", command=lambda: excluir_despesa(categoria_excluir_despesa.get())).pack(pady=10)
        
        # Espaço para excluir categoria
        frame_excluir_categoria = Frame(container_excluir, bg=bg_color)
        frame_excluir_categoria.pack(pady=10, side='left', padx=20)
        ttk.Label(frame_excluir_categoria, text="Excluir Categoria", font=("Helvetica", 10), background=bg_color).pack(pady=10)
        
        ttk.Label(frame_excluir_categoria, text="Categoria:", background=bg_color).pack()
        categorias_excluir_categoria = view.ver_categorias(conexao_bd, 'id')
        categoria_excluir_categoria = ttk.Combobox(frame_excluir_categoria, values=categorias_excluir_categoria)
        categoria_excluir_categoria.pack(pady=5)
        
        Button(frame_excluir_categoria, text="Excluir Categoria", command=lambda: excluir_categoria(categoria_excluir_categoria.get())).pack(pady=10)

        return aba3

def adicionar_receita(data, valor, categoria):
    try: 
        # Limpar dados atuais na Treeview
        valor = float(valor)
        for row in tabela_receitas.get_children():
            tabela_receitas.delete(row)   

        view.inserir_receita(data, valor, categoria)
        
        for receita in view.ver_Saldo_e_investimentos_full(conexao_bd):
            tabela_receitas.insert('', 'end', text='', values=(receita[0], receita[1], receita[2], receita[3]))    
    except:
        print('O valor deve ser numeral')

        messagebox.showinfo('Deve ser um numeral')    

def adicionar_despesa(data, valor, categoria):
    try:
        int(valor), float(valor)
            # Limpar dados atuais na Treeview
        for row in tabela_despesas.get_children():
            tabela_despesas.delete(row)   

        view.inserir_despesa(data, valor, categoria)
        
        for despesa in view.ver_Gastos_full(conexao_bd):
            tabela_despesas.insert('', 'end', text='', values=(despesa[0], despesa[1], despesa[2], despesa[3]))
    except:
        print('O valor deve ser numeral')   
        messagebox.showinfo('Deve ser um numeral')  

def adicionar_categoria(categoria):
    try:
        categoria = int(categoria)
        print('O valor deve ser um texto')
        messagebox.showinfo('Deve ser um texto')  
           
    except:
        categoria = str(categoria)
        # Limpar dados atuais na Treeview
        for row in tabela_categorias.get_children():
            tabela_categorias.delete(row)   

        view.inserir_categoria(categoria)
        
        for categoria in view.ver_categorias_full(conexao_bd):
            tabela_categorias.insert('', 'end', text='', values=(categoria[0], categoria[1]))

def excluir_receita(receita):
    view.deletar_Saldo_e_investimentos(receita)
    
    for row in tabela_receitas.get_children():
            tabela_receitas.delete(row)  
    
    for receita in view.ver_Saldo_e_investimentos_full(conexao_bd):
            tabela_receitas.insert('', 'end', text='', values=(receita[0], receita[1], receita[2], receita[3]))

def excluir_despesa(despesa):
    view.deletar_Gastos(despesa)
    
    for row in tabela_despesas.get_children():
            tabela_despesas.delete(row)   

    for despesa in view.ver_Gastos_full(conexao_bd):
            tabela_despesas.insert('', 'end', text='', values=(despesa[0], despesa[1], despesa[2], despesa[3]))

def excluir_categoria(categoria):
    view.deletar_categoria(categoria)
    
    for row in tabela_categorias.get_children():
            tabela_categorias.delete(row)   

    for categoria in view.ver_categorias_full(conexao_bd):
            tabela_categorias.insert('', 'end', text='', values=(categoria[0], categoria[1]))
    
# Atualizar as comboboxes de categoria após excluir uma categoria

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




