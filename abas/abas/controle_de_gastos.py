import sys
import numpy as np
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
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

# Criando gráfico de pizza
fig = Figure(figsize=(7,4), facecolor=co2)
ax = fig.add_subplot(111)

opções = ["Alimentação",
          "Transporte",
          "Saúde",
          "Lazer","Educação","Gastos fixos"]
valores=[200,300,450,100,300]

data = [float(x) for x in valores]
Categorias = [x for x in opções]


def func(pct, allvals):
    absolute = int(np.round(pct / 100. * np.sum(allvals)))
    return f"{pct:.1f}%\n(R${absolute:d})"

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
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

janela.mainloop()
