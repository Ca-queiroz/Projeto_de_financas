from tkinter import Label
import sys
import numpy as np
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

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

# Criando janela
janela = tk.Tk()
janela.title("Minha Aplicação")
janela.geometry("720x1280")
janela.configure(background=co2)
janela.resizable(width=False, height=False)

# Configurando o estilo
style = ttk.Style(janela)
style.theme_use("clam")

# Corrigindo a configuração da fonte e a cor de fundo das abas
style.configure('TNotebook.Tab',
                background=co10,
                foreground=co1,
                padding=[90, 15],
                font=("Helvetica", 12),
                wraplength=170)
style.map('TNotebook.Tab',
          background=[('selected', co1)],
          foreground=[('selected', co10)],
          font=[('selected', ('Helvetica', 12, 'bold')), ('!selected', ('Helvetica', 12, 'bold'))])

# Criando um widget Notebook para as abas
notebook = ttk.Notebook(janela)
notebook.pack(fill='both', expand=True)

# Criando as frames para cada aba
aba1 = ttk.Frame(notebook)
aba2 = ttk.Frame(notebook)
aba3 = ttk.Frame(notebook)

# Adicionando as frames ao Notebook
notebook.add(aba1, text='  Fluxo de\n Finanças')
notebook.add(aba2, text='Controle de\n    Gastos')
notebook.add(aba3, text='        Tabela de\n Receitas e Despesas')

# Criando frame para o título nas abas
Framecima1 = tk.Frame(aba1, width=720, height=170, bg=co1, relief="flat")
Framecima1.pack(side=tk.TOP, fill=tk.X)
Framecima2 = tk.Frame(aba2, width=720, height=170, bg=co1, relief="flat")
Framecima2.pack(side=tk.TOP, fill=tk.X)
Framecima3 = tk.Frame(aba3, width=720, height=170, bg=co1, relief="flat")
Framecima3.pack(side=tk.TOP, fill=tk.X)

Framebaixo1 = tk.Frame(aba1, width=720, height=1280, bg=co2, relief="flat")
Framebaixo1.pack(side=tk.TOP, fill=tk.X)
Framebaixo2 = tk.Frame(aba2, width=720, height=1280, bg=co2, relief="raised")
Framebaixo2.pack(side=tk.TOP, fill=tk.X)
Framebaixo3 = tk.Frame(aba3, width=720, height=1280, bg=co2, relief="flat")
Framebaixo3.pack(side=tk.TOP, fill=tk.X)

# Adicionando os títulos
imagem1 = ImageTk.PhotoImage(file="abas/abas/fluxodeinançasimg.png")
label_imagem1 = tk.Label(Framecima1, image=imagem1)
label_imagem1.pack()
imagem2 = ImageTk.PhotoImage(file="abas/abas/controledegastosimg.png")
label_imagem2 = tk.Label(Framecima2, image=imagem2)
label_imagem2.pack()
imagem3 = ImageTk.PhotoImage(file="abas/abas/receitaedespesasimg.png")
label_imagem3 = tk.Label(Framecima3, image=imagem3)
label_imagem3.pack()

#criando percentagem 

def percentagem():
  nome1 = Label(Framebaixo1, text='Percentagem da Receita Gasta', height=1, font=('Georgia 14'), bg = co2, fg=co4 )
  nome1.place(x = 5 , y = 7)

  style = ttk.Style()
  style.theme_use('default')
  style.configure('black.Horizontal.TProgressbar', background='#B1E492')
  style.configure('TProgressbar', thickness = 25)


  bar = ttk.Progressbar(Framebaixo1, length=180)
  bar.place(x=10, y=35)
  bar['value'] = 50

  valor = 50

  percentagem1 = Label(Framebaixo1, text='{:,.2f}'.format(valor), height=1, font=('Georgia 14'), bg = co2, fg=co4 )
  percentagem1.place(x = 200 , y = 35)

#função para gráfico bars

def grafico_bar():
  lista_categorias = ['Renda', 'Despesas', 'Saldo']
  lista_valores = [300, 2000, 6236]

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
  canva.get_tk_widget().place(x=10, y=70)

# funcao de resumo

def resumo():
  valor = [500, 600, 420]

  l_linha = Label(Framebaixo1, text = '', width = 215, height = 1, font = ('Arial 1'), bg = '#545454')
  l_linha.place(x=309, y = 52)
  l_sumario = Label(Framebaixo1, text = 'Renda Mensal Total        '.upper(), font = ('Georgia 12'), bg = co2, fg = co4)
  l_sumario.place(x=309, y = 35)
  l_sumario = Label(Framebaixo1, text = 'R$ {:,.2F}'.format(valor[0]), font = ('Arial 17'), bg = co2, fg = co4)
  l_sumario.place(x=309, y = 70)


  l_linha = Label(Framebaixo1, text = '', width = 215, height = 1, font = ('Arial 1'), bg = '#545454')
  l_linha.place(x=309, y = 132)
  l_sumario = Label(Framebaixo1, text = 'Despesa Mensal Total       '.upper(), font = ('Georgia 12'), bg = co2, fg = co4)
  l_sumario.place(x=309, y = 115)
  l_sumario = Label(Framebaixo1, text = 'R$ {:,.2F}'.format(valor[1]), font = ('Arial 17'), bg = co2, fg = co4)
  l_sumario.place(x=309, y = 150)


  l_linha = Label(Framebaixo1, text = '', width = 215, height = 1, font = ('Arial 1'), bg = '#545454')
  l_linha.place(x=309, y = 207)
  l_sumario = Label(Framebaixo1, text = 'Saldo Total                          '.upper(), font = ('Georgia 12'), bg = co2, fg = co4)
  l_sumario.place(x=309, y = 190)
  l_sumario = Label(Framebaixo1, text = 'R$ {:,.2F}'.format(valor[2]), font = ('Arial 17'), bg = co2, fg = co4)
  l_sumario.place(x=309, y = 230)

#aaa


percentagem()
grafico_bar()
resumo()

janela.mainloop()

