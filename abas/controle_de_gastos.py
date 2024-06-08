from tkinter import Label, Entry, ttk, Frame
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import view
import sqlite3 as lite
from matplotlib.figure import Figure
import numpy as np
import pandas as pd

global conexao_bd
conexao_bd = lite.connect('dados.bd')

global co0
global co1
global co2
global co3
global co4
global co5
global co6
global co7
global co8
global co9
global co10
global co11


co0 = "#2e2d2b"  # preta
co1 = "#feffff"  # branca
co2 = "#B1E492"  # verde
co3 = "#38576b"  # valor
co4 = "#403d3d"  # letra
co5 = "#e06636"  # - profit
co6 = "#5588bb"  # azul
co7 = "#3fbfb9"  #
co8 = "#263238"
co9 = "#e9edf5"
co10 = "#498B48"
co11= "#0C793E"
# Criando gráfico de pizza
fig = Figure(figsize=(9,5), facecolor=co2,)
ax = fig.add_subplot(111)

# Categorias = ['Alimentação', 'Lazer', 'Viagem']
# data = [100, 200, 300]
# data = [valores, Categorias]

def criar_aba2(notebook, bg_color):
    aba2 = Frame(notebook, bg=bg_color)  # Usando Frame do Tkinter para suportar a configuração de cor de fundo
    notebook.add(aba2, text='Controle de Gastos')
    Framecima = Frame(aba2, width=1280, height=150, relief="flat")
    Framecima.pack(side='top', fill='both')
    imagem1 = Image.open("abas/images/controledegastosimg.png")
    imagem1 = ImageTk.PhotoImage(imagem1)
    label_imagem1 = tk.Label(Framecima, image=imagem1)
    label_imagem1.image = imagem1  # Garante que a imagem não seja apagada pela coleta de lixo
    label_imagem1.pack()
    global Framebaixo2
    Framebaixo2 = tk.Frame(aba2, width=720, height=1280, bg=co2, relief="raised")
    Framebaixo2.pack(side=tk.TOP, fill=tk.X)

    dados = view.ver_gastos_agrupados_por_categoria(conexao_bd)
    categorias, valores = zip(*dados)

    # Converter as tuplas resultantes em listas
    Categorias = list(categorias)
    data = list(valores)

    wedges, texts, autotexts = ax.pie(data, autopct=lambda pct: func(pct, data),
                                  textprops=dict(color=co0, fontsize=14))
    legend = ax.legend(wedges, Categorias,
                    title="Categorias",
                    loc="center left",
                    bbox_to_anchor=(1, 0, 0.5, 1),
                    fontsize=11)

    legend.get_title().set_color(co11)
    legend.get_title().set_fontname("Georgia")
    legend.get_title().set_fontsize(14)
    legend.get_title().set_fontweight("bold")

    for autotext in autotexts:
        autotext.set_fontsize(8)
        autotext.set_fontweight("bold")
        autotext.set_fontname("Arial")
        autotext.set_color(co1)

    ax.set_title("Acompanhe seus gastos mensais aqui, e se planeje\n melhor para o mês seguinte",fontsize=14, color=co11,y=0.93,fontname="Georgia")

    # Converte o gráfico de pizza para um widget Tkinter e adiciona à aba2
    canvas = FigureCanvasTkAgg(fig, master=Framebaixo2)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH, expand=1)

    
    return aba2



# Ponte entre grafico e tabela
def pie_valores():
    gastos = view.ver_Gastos_2()
    tabela_lista =[]
    for i in gastos:
        tabela_lista.append(i)
    dataframe = pd.DataFrame(tabela_lista, columns=['id','Categorias','Data', 'Valor'])
    dataframe= dataframe.groupby('Categorias')['valor'].sum()
    
    lista_quantias= dataframe.values.tolist()
    lista_categorias=[]

    for i in dataframe.index:
        lista_categorias.append(i)
    
    return([lista_categorias, lista_quantias])

    view.ver_gastos_agrupados_por_categoria(conexao_bd)


def func(pct, allvals):
    absolute = int(np.round(pct / 100. * np.sum(allvals)))
    return f"{pct:.1f}%\n(R${absolute:d})"




# --------------------------------------------
