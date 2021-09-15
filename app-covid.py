from tkinter import *

#################### Cores ####################
co0 = "#000000"  # black
co1 = "#cc1d4e"  # red
co2 = "#feffff"  # white
co3 = "#0074eb"  # blue
co4 = "#435e5a"  # #435e5a
co5 = "#59b356"  # green
co6 = "#d9d9d9"  # grey

################ criar a janela principal do aplicativo ################
janela = Tk()

janela.resizable(width=FALSE, height=FALSE)
janela.geometry('835x360')
janela.title('')
janela.configure(bg=co6)

################ criando frames ################

app_nome_frame = Frame(janela, width=840, height=50, bg=co1, relief='flat')
app_nome_frame.grid(row=0, column=0,columnspan=3, sticky=NSEW)

mostrar_frame_infectados = Frame(janela, width=220, height=100, bg=co3, relief='flat')
mostrar_frame_infectados.grid(row=1, column=0, sticky=NW, pady=5, padx=5)

mostrar_frame_recuperados = Frame(janela, width=220, height=100, bg=co3, relief='flat')
mostrar_frame_recuperados.grid(row=1, column=1, sticky=NW, pady=5, padx=5)

mostrar_frame_mortes = Frame(janela, width=220, height=100, bg=co3, relief='flat')
mostrar_frame_mortes.grid(row=1, column=2, sticky=NW, pady=5, padx=5)


app_nome_frame = Frame(janela, width=840, height=50, bg=co5, relief='flat')
app_nome_frame.grid(row=2, column=0,columnspan=3, sticky=NSEW)

janela.mainloop()
