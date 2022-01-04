
from random import random
from tkinter import *
import time

def jackpot():
    saida = []
    ganhos = 0
    ss = 0
    rodada = []
    aposta = int(botao_a.get())
    for x in range(3):
        rodada.append(round(random()*10, 2))
        if 0 <= rodada[x] <= 1.42:
            saida.append('$')
        elif 1.42 < rodada[x] <= 2.85:
            saida.append('%')
        elif 2.85 < rodada[x] <= 4.27:
            saida.append('&')
        elif 4.27 < rodada[x] <= 5.69:
            saida.append('£')
        elif 5.69 < rodada[x] <= 7.11:
            saida.append('§')
        elif 7.11 < rodada[x] <= 8.53:
            saida.append('¢')
        elif 8.53 < rodada[x] <= 10:
            saida.append('#')

    if saida[0] == saida[1] == saida[2]:
        if saida[0] == '%':
                ganhos = aposta * 25
        elif saida[0] == '&':
                ganhos = aposta * 50
        elif saida[0] == '£':
                ganhos = aposta * 75
        elif saida[0] == '§':
                ganhos = aposta * 100
        elif saida[0] == '¢':
                ganhos = aposta * 250
        elif saida[0] == '#':
                ganhos = aposta * 1000
    elif '$' in saida:
        for x in range(3):
            if saida[x] == '$':
                ss = ss + 1
        if ss == 1:
            ganhos = aposta * 2   
        elif ss == 2:
            ganhos = aposta * 5
        elif ss == 3:
            ganhos = aposta * 500

    simbolos['text'] = '  '+saida[0]+'  '+saida[1]+'  '+saida[2]
    apostado['text'] = f'Last bet - {str(aposta)}'
    ganho['text'] = f'Last gain - {str(ganhos)}'


def vezes(func, v, aposta):
    for x in range(v):
        func(aposta)

def janela_infos():
    texto_info = """
    Combinations
    $ - 2x
    $$ - 5x
    $$$ - 500x
    %%% - 25x
    &&& - 50x
    £££ - 75x
    §§§ - 100x
    ¢¢¢ - 250x
    ### - 1000x
    """ 
    janela2 = Tk()
    janela2.title('Info')

    texto_informa = Label(janela2, text=texto_info)
    texto_informa.pack()

    janela2.mainloop()

def apagar_jack():
    simbolos['text'] = '       '

janela = Tk()
janela.title('JACKPOT')

texto_informa = Label(janela, text='Your bet: ')
texto_informa.grid(column=0, row=0)

apostado = Label(janela, text='Last bet - 0')
apostado.grid(column=0, row=1)

ganho = Label(janela, text='Last gain - 0')

ganho.grid(column=0, row=2)

botao_a = Entry()
botao_a.grid(column=1, row=0)

simbolos = Label(janela, text='       ')
simbolos.grid(column=1, row=1)

botao = Button(text='PLAY',command=jackpot)
botao.grid(column=1, row=2)

botao_info = Button(text='Info', command=janela_infos)
botao_info.grid(column=2, row=2)

botao_limpar = Button(text='C', command=apagar_jack)
botao_limpar.grid(column=2,row=1)

janela.mainloop()