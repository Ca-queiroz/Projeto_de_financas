from tkinter import *
from tkinter import Tk, ttk 
from abas.fluxo_de_finanças import criar_aba1
from abas.controle_de_gastos import criar_aba2
from abas.tabela_de_receitas_e_despesas import criar_aba3 

co0 = "#2e2d2b" #preta
co1 = "#feffff" #branca
co2 = "#99bb55" #verde
co3 = "#38576b" #valor
co4 = "#403d3d" #letra
co5 = "#e06636" #- profit
co6 = "#5588bb" #azul
co7 = "#3fbfb9" #
co8 = "#263238"
co9 = "#e9edf5"

colors = ["#5588bb", "#66bbbb", "#99bb55", "#ee9944", "#444466", "bb5555"]

#criando janela 
janela = Tk()
janela.title()
janela.geometry("1280x800")
janela.configure(background=co2)
janela.resizable(width=FALSE, height=FALSE)

style=ttk.Style(janela)
style.theme_use("clam")

# Criando um widget Notebook para as abas
notebook = ttk.Notebook(janela)
notebook.pack(fill='both', expand=True)

#Criando as abas
criar_aba1(notebook, co2)
criar_aba2(notebook, co2)
criar_aba3(notebook, co2)


# Iniciando o loop de eventos do Tkinter
janela.mainloop()
