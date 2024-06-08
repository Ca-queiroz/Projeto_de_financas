from tkinter import Label, Entry, ttk, Frame
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import view
import sqlite3 as lite

global conexao_bd
conexao_bd = lite.connect('dados.bd')

def criar_aba1(notebook, bg_color):
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
    global colors

    # Definindo cores
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
    co11="#0C793E"

    colors = ['#5588bb', '#66bbbb', '#99bb55', '#ee9944', '#444466', '#bb5555']

    aba1 = Frame(notebook, bg=bg_color)  # Usando Frame do Tkinter para suportar a configuração de cor de fundo
    notebook.add(aba1, text='Fluxo de Finanças')
    Framecima = Frame(aba1, width=1280, height=150, relief="flat")
    Framecima.pack(side='top', fill='both')
    imagem1 = Image.open("abas/images/fluxodeinançasimg.png")
    imagem1 = ImageTk.PhotoImage(imagem1)
    label_imagem1 = tk.Label(Framecima, image=imagem1)
    label_imagem1.image = imagem1  # Garante que a imagem não seja apagada pela coleta de lixo
    label_imagem1.pack()
    container_adicionar = Frame(aba1, bg=bg_color)
    container_adicionar.pack(pady=20, side='top')
    Framebaixo1 = tk.Frame(container_adicionar, width=720, height=1280, bg=co2, relief="flat")
    Framebaixo1.pack(side='left', fill='both')  

    percentagem(Framebaixo1)
    grafico_bar(Framebaixo1)
    resumo(Framebaixo1)
    return aba1

def percentagem(Framebaixo1):
    nome1 = Label(Framebaixo1, text='Receita Gasta', height=1, font=('Georgia 14'), bg = co2, fg=co4 )
    nome1.place(x = 20 , y = 7)

    style = ttk.Style(Framebaixo1)
    style.theme_use('default')
    style.configure('black.Horizontal.TProgressbar', background='#B1E492')
    style.configure('TProgressbar', thickness = 25)

    percentual_gasto = calcular_percentual_receita_x_despesa()


    bar = ttk.Progressbar(Framebaixo1, length=180)
    bar.place(x=25, y=35)
    bar['value'] = percentual_gasto

    valor = percentual_gasto

    percentagem1 = Label(Framebaixo1, text='{:,.2f} %'.format(valor), height=1, font=('Georgia 14'), bg = co2, fg=co4 )
    percentagem1.place(x = 200 , y = 35)

#função para gráfico bars

def grafico_bar(Framebaixo1):    
    receita_sum = view.ver_Saldo_e_investimentos_sum(conexao_bd)
    despesa_sum = view.ver_Gastos_sum(conexao_bd)
    saldo = int(receita_sum) - int(despesa_sum)

    lista_categorias = ['Renda', 'Despesas', 'Saldo']
    lista_valores = [receita_sum, despesa_sum, saldo]

    figura = plt.Figure(figsize=(4, 3.45), dpi = 60)
    ax = figura.add_subplot(111)

    ax.bar(lista_categorias, lista_valores, color = colors, width =0.9)

    c = 0

    for i in ax.patches:
        ax.text(i.get_x()-.001, i.get_height()+.5,
        str('{:,.0f}'.format(lista_valores[c])), fontsize = 17, fontstyle = 'italic' , verticalalignment = 'bottom', color = 'dimgrey')
        c += 1 

    ax.set_xticklabels(lista_categorias,fontsize=16)

    ax.patch.set_facecolor('#ffffff')
    ax.spines['bottom'].set_color('#CCCCCC')
    ax.spines['bottom'].set_linewidth(1)
    ax.spines['right'].set_linewidth(0)
    ax.spines['top'].set_linewidth(0)
    ax.spines['left'].set_color('#CCCCCC')
    ax.spines['left'].set_linewidth(1)

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.tick_params(bottom=False, left=False)
    ax.set_axisbelow(True)
    ax.yaxis.grid(False, color='#EEEEEE')
    ax.xaxis.grid(False)

    canva = FigureCanvasTkAgg(figura, Framebaixo1)
    canva.get_tk_widget().place(x=25, y=90)

    # funcao de resumo

def resumo(Framebaixo1):
    receita_sum = view.ver_Saldo_e_investimentos_sum(conexao_bd)
    despesa_sum = view.ver_Gastos_sum(conexao_bd)
    saldo = int(receita_sum) - int(despesa_sum)
    valor = [receita_sum, despesa_sum, saldo]

    l_linha = Label(Framebaixo1, text = '', width = 215, height = 1, font = ('Arial 1'), bg = '#545454')
    l_linha.place(x=350, y = 52)
    l_sumario = Label(Framebaixo1, text = 'Renda Mensal Total        '.upper(), font = ('Georgia 12'), bg = co2, fg = co4)
    l_sumario.place(x=350, y = 35)
    l_sumario = Label(Framebaixo1, text = 'R$ {:,.2F}'.format(valor[0]), font = ('Arial 17'), bg = co2, fg = co4)
    l_sumario.place(x=350, y = 70)


    l_linha = Label(Framebaixo1, text = '', width = 215, height = 1, font = ('Arial 1'), bg = '#545454')
    l_linha.place(x=350, y = 132)
    l_sumario = Label(Framebaixo1, text = 'Despesa Mensal Total       '.upper(), font = ('Georgia 12'), bg = co2, fg = co4)
    l_sumario.place(x=350, y = 115)
    l_sumario = Label(Framebaixo1, text = 'R$ {:,.2F}'.format(valor[1]), font = ('Arial 17'), bg = co2, fg = co4)
    l_sumario.place(x=350, y = 150)


    l_linha = Label(Framebaixo1, text = '', width = 215, height = 1, font = ('Arial 1'), bg = '#545454')
    l_linha.place(x=350, y = 207)
    l_sumario = Label(Framebaixo1, text = 'Saldo Total                          '.upper(), font = ('Georgia 12'), bg = co2, fg = co4)
    l_sumario.place(x=350, y = 190)
    l_sumario = Label(Framebaixo1, text = 'R$ {:,.2F}'.format(valor[2]), font = ('Arial 17'), bg = co2, fg = co4)
    l_sumario.place(x=350, y = 230)

def calcular_percentual_receita_x_despesa():
    receita_sum = view.ver_Saldo_e_investimentos_sum(conexao_bd)
    despesa_sum = view.ver_Gastos_sum(conexao_bd)

    receita_sum = receita_sum if receita_sum is not None else 0
    despesa_sum = despesa_sum if despesa_sum is not None else 0

    # Calcular o percentual de receita_sum gasta
    if receita_sum != 0:
        percentual_gasto = (despesa_sum / receita_sum) * 100
    else:
        percentual_gasto = 0

    return percentual_gasto

# co0 = "#2e2d2b"  # preta
# co1 = "#feffff"  # branca
# co2 = "#B1E492"  # verde
# co3 = "#38576b"  # valor
# co4 = "#403d3d"  # letra
# co5 = "#e06636"  # - profit
# co6 = "#5588bb"  # azul
# co7 = "#3fbfb9"  #
# co8 = "#263238"
# co9 = "#e9edf5"
# co10 = "#498B48"
# co11="#0C793E"

# colors = ['#5588bb', '#66bbbb', '#99bb55', '#ee9944', '#444466', '#bb5555']

# # Criando janela
# janela = tk.Tk()
# janela.title("Minha Aplicação")
# janela.geometry("720x1280")
# janela.configure(background=co2)
# janela.resizable(width=False, height=False)

# # Configurando o estilo
# style = ttk.Style(janela)
# style.theme_use("clam")

# # Corrigindo a configuração da fonte e a cor de fundo das abas
# style.configure('TNotebook.Tab',
#                 background=co10,
#                 foreground=co1,
#                 padding=[90, 15],
#                 font=("Helvetica", 12),
#                 wraplength=170)
# style.map('TNotebook.Tab',
#           background=[('selected', co1)],
#           foreground=[('selected', co10)],
#           font=[('selected', ('Helvetica', 12, 'bold')), ('!selected', ('Helvetica', 12, 'bold'))])

# # Criando um widget Notebook para as abas
# notebook = ttk.Notebook(janela)
# notebook.pack(fill='both', expand=True)

# # Criando as frames para cada aba
# aba1 = ttk.Frame(notebook)
# aba2 = ttk.Frame(notebook)
# aba3 = ttk.Frame(notebook)

# # Adicionando as frames ao Notebook
# notebook.add(aba1, text='  Fluxo de\n Finanças')
# notebook.add(aba2, text='Controle de\n    Gastos')
# notebook.add(aba3, text='        Tabela de\n Receitas e Despesas')

# # Criando frame para o título nas abas
# Framecima1 = tk.Frame(aba1, width=720, height=170, bg=co1, relief="flat")
# Framecima1.pack(side=tk.TOP, fill=tk.X)
# Framecima2 = tk.Frame(aba2, width=720, height=170, bg=co1, relief="flat")
# Framecima2.pack(side=tk.TOP, fill=tk.X)
# Framecima3 = tk.Frame(aba3, width=720, height=170, bg=co1, relief="flat")
# Framecima3.pack(side=tk.TOP, fill=tk.X)

# Framebaixo1 = tk.Frame(aba1, width=720, height=1280, bg=co2, relief="flat")
# Framebaixo1.pack(side=tk.TOP, fill=tk.X)
# Framebaixo2 = tk.Frame(aba2, width=720, height=1280, bg=co2, relief="raised")
# Framebaixo2.pack(side=tk.TOP, fill=tk.X)
# Framebaixo3 = tk.Frame(aba3, width=720, height=1280, bg=co2, relief="flat")
# Framebaixo3.pack(side=tk.TOP, fill=tk.X)

# # Adicionando os títulos
# imagem1 = ImageTk.PhotoImage(file="abas/abas/fluxodeinançasimg.png")
# label_imagem1 = tk.Label(Framecima1, image=imagem1)
# label_imagem1.pack()
# imagem2 = ImageTk.PhotoImage(file="abas/abas/controledegastosimg.png")
# label_imagem2 = tk.Label(Framecima2, image=imagem2)
# label_imagem2.pack()
# imagem3 = ImageTk.PhotoImage(file="abas/abas/receitaedespesasimg.png")
# label_imagem3 = tk.Label(Framecima3, image=imagem3)
# label_imagem3.pack()

#criando percentagem 




# janela.mainloop()

