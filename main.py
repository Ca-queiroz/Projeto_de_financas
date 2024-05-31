#COMEÇANDO A DESENHAR A TELA - PASTA

from tkinter import *
from tkinter import Tk, ttk # tkinter é uma bilioteca que ele chama para criação de tela com py - interface gráfica do py

#cores 

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
janela.geometry("720x1280")
janela.configure(background=co2)
janela.resizable(width=FALSE, height=FALSE)

style= ttk.Style(janela)
style.theme_use("clam")


#Crinado frames para divisão de tela
frame_de_cima = Frame (janela, width= 720,height=50, bg= co0, relief = "flat")
frame_de_cima.grid(row=0,column=0)

frame_do_meio = Frame (janela, width= 720,height=361, bg= co0, pady = 20, relief = "raised")
frame_do_meio.grid(row=1,column=0, pady=1, padx=0, sticky=NSEW)

frame_de_baixo = Frame (janela, width= 720,height=300, bg= co2, pady = 20, relief = "flat")
frame_de_baixo.grid(row=2,column=0, pady=0, padx=0, sticky=NSEW)

janela.mainloop()



teste Bianca