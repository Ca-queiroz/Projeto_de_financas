from tkinter import ttk

def criar_aba2(notebook):
    aba2 = ttk.Frame(notebook)
    notebook.add(aba2, text='Controle de Gastos')
    ttk.Label(aba2, text="Conteúdo da Aba 2", font=("Arial", 24)).pack(pady=50)
    return aba2