from tkinter import *
from tkinter import Tk, ttk 
from PIL import Image, ImageTk
from abas.fluxo_de_finanças import criar_aba1
from abas.controle_de_gastos import criar_aba2
from abas.tabela_de_receitas_e_despesas import criar_aba3 

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

#criando janela 
janela = Tk()
janela.title()
janela.geometry("1280x1000")
janela.configure(background=co2)
janela.resizable(width=FALSE, height=FALSE)

style=ttk.Style(janela)
style.theme_use("clam")

# Corrigindo a configuração da fonte e a cor de fundo das abas
style.configure('TNotebook.Tab',
                background=co10,
                foreground=co1,
                # padding=[90, 15],
                font=("Helvetica", 12),
                wraplength=200)
style.map('TNotebook.Tab',
          background=[('selected', co1)],
          foreground=[('selected', co10)],
          font=[('selected', ('Helvetica', 12, 'bold')), ('!selected', ('Helvetica', 12, 'bold'))])

# Criando um widget Notebook para as abas
notebook = ttk.Notebook(janela)
notebook.pack(fill='both', expand=True)

#Criando as abas
aba3 = criar_aba3(notebook, co2)
aba1 = criar_aba1(notebook, co2)
aba2 = criar_aba2(notebook, co2)

# # Carregando as imagens para as abas
# imagem1 = Image.open("abas/images/fluxodefinancasimg.png")
# imagem1 = ImageTk.PhotoImage(imagem1)

# imagem2 = Image.open("abas/images/controledegastosimg.png")
# imagem2 = ImageTk.PhotoImage(imagem2)

# imagem3 = Image.open("abas/images/receitaedespesasimg.png")
# imagem3 = ImageTk.PhotoImage(imagem3)

# # Adicionando as abas ao notebook com as imagens
# notebook.add(aba1, image=imagem1, compound='left')
# notebook.add(aba2, image=imagem2, compound='left')
# notebook.add(aba3, image=imagem3, compound='left')



# Iniciando o loop de eventos do Tkinter
janela.mainloop()

# # Criando frame para o título nas abas
# Framecima1 = Tk.Frame(aba1, width=720, height=170, bg=co1, relief="flat")
# Framecima1.pack(side=Tk.TOP, fill=Tk.X)
# Framecima2 = Tk.Frame(aba2, width=720, height=170, bg=co1, relief="flat")
# Framecima2.pack(side=Tk.TOP, fill=Tk.X)
# Framecima3 = Tk.Frame(aba3, width=720, height=170, bg=co1, relief="flat")
# Framecima3.pack(side=Tk.TOP, fill=Tk.X)

# Framebaixo1 = Tk.Frame(aba1, width=720, height=1280, bg=co2, relief="flat")
# Framebaixo1.pack(side=Tk.TOP, fill=Tk.X)
# Framebaixo2 = Tk.Frame(aba2, width=720, height=1280, bg=co2, relief="raised")
# Framebaixo2.pack(side=Tk.TOP, fill=Tk.X)
# Framebaixo3 = Tk.Frame(aba3, width=720, height=1280, bg=co2, relief="flat")
# Framebaixo3.pack(side=Tk.TOP, fill=Tk.X)

# # Adicionando os títulos
# imagem1 = ImageTk.PhotoImage(file="abas/images/fluxodeinançasimg.png")
# label_imagem1 = Tk.Label(Framecima1, image=imagem1)
# label_imagem1.pack()
# imagem2 = ImageTk.PhotoImage(file="abas/images/controledegastosimg.png")
# label_imagem2 = Tk.Label(Framecima2, image=imagem2)
# label_imagem2.pack()
# imagem3 = ImageTk.PhotoImage(file="abas/images/receitaedespesasimg.png")
# label_imagem3 = Tk.Label(Framecima3, image=imagem3)
# label_imagem3.pack()