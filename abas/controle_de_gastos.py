from tkinter import ttk, Frame

def criar_aba2(notebook, bg_color):
    aba2 = Frame(notebook, bg=bg_color)  # Usando Frame do Tkinter para suportar a configuração de cor de fundo
    notebook.add(aba2, text='Controle de Gastos')
    ttk.Label(aba2, text="Conteúdo da Aba 2", font=("Arial", 24), background=bg_color).pack(pady=50)
    return aba2