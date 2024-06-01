from tkinter import ttk

def criar_aba1(notebook):
    aba1 = ttk.Frame(notebook)
    notebook.add(aba1, text='Fluxo de Finanças')
    ttk.Label(aba1, text="Conteúdo da Aba 1", font=("Arial", 24)).pack(pady=50)
    return aba1
