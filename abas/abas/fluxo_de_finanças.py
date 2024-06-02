from tkinter import ttk, Frame

def criar_aba1(notebook, bg_color):
    aba1 = Frame(notebook, bg=bg_color)  # Usando Frame do Tkinter para suportar a configuração de cor de fundo
    notebook.add(aba1, text='Fluxo de Finanças')
<<<<<<< HEAD:abas/fluxo_de_financas.py
    ttk.Label(aba1, text="Conteúdo da Aba 1", font=("Arial", 24), background=bg_color).pack(pady=50)
    return aba1
=======
    ttk.Label(aba1, text="Conteúdo da Aba 1", font=("Arial", 24)).pack(pady=50)
    return aba1
>>>>>>> main:abas/abas/fluxo_de_finanças.py
