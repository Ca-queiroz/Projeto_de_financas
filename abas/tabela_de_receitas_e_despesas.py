from tkinter import ttk

def criar_aba3(notebook):
    aba3 = ttk.Frame(notebook)
    notebook.add(aba3, text='Tabela de Receitas e Despesas')
    ttk.Label(aba3, text="Conteúdo da Aba 3", font=("Arial", 24)).pack(pady=50)
    return aba3