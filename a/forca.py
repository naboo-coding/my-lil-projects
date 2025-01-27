from tkinter import *
import random

tentativas = 10
master=None

# Configuração para as palavras aleatórias
def randomizar_palavras():
    global palavras
    palavras = ['tapete', 'cachorro', 'pirata', 'caravela', 'onça', 'sopa', 'barco', 'flores', 'paraiso', 'constitucionalissimamente', 'arvore', 'almofada']
    global resposta
    resposta = random.choice(palavras)  # Escolhe de forma aleatória uma palavra da variável 'palavras'
    global letras
    letras = ['_' for letra in resposta]

#
#
# 5 def's seguintes ciram as janelas
#
#
def janela1_open():
    global janela1
    janela1 = Tk()
    janela1.title("The Hanging Man")

def janela2_open():
    global janela2
    janela2 = Tk()
    janela2.title("The Hanging Man")
    janela2.geometry("500x190")

def janela3_open():
    global janela3
    janela3 = Tk()
    janela3.title("The Hanging Man")
    janela3.geometry("400x250")

def janela4_open():
    global janela4
    janela4 = Tk()
    janela4.title("The Hanging Man")
    janela4.geometry("200x190")

def janela5_open():
    global janela5
    janela5 = Tk()
    janela5.title("The Hanging Man")
    janela5.geometry("200x190")

# Menu inicial
def abre_textos1():
    janela1_open()
    global janela1
    
    texto = Label(janela1, text="Welcome! Are you ready??")
    texto.grid(column=1,row=0, padx=25, pady=25)
    texto.pack
    texto["fg"] = "darkblue"
      # Botão de start: 
    buttun1 = Button(janela1, text="Start", command=botao_start)
    buttun1.grid(column=1, row=1, padx=25, pady=0)
    buttun1.pack
    buttun1["fg"] = "darkgreen"
      # Botão pra sair:
    buttun2 = Button(janela1, text="LEMME OUT!!", command=quit)
    buttun2.grid(column=1, row=2, padx=25, pady=25)
    buttun2.pack
    buttun2["fg"] = "darkred"

    janela1.mainloop()

# Menu explicando o jogo
def botao_start():
    janela1.withdraw()
    janela2_open()
    global janela2

    # Containers:
    container1 = Frame(janela2)
    container1["pady"] = 30
    container1.pack()

    # Widgets
    texto2 = Label(container1, text="How does this game work?")
    texto2.pack(side=TOP)
    texto2["fg"] = "darkred"
    texto2["font"] = "14"
    texto2["pady"] = 2

    texto1 = Label(container1, text="Guess a letter or word, if you dont get it right, you lose lives")
    texto1.pack()
    texto1["pady"] = 1

    texto3 = Label(janela2, text="If you get a letter wrong, you lose 1 of your tries, you got 10")
    texto3.pack()
    texto3["font"] = "arial, 7"
    texto3["fg"] = "red"
    texto3["pady"] = 5

      # Botão
    alright = Button(janela2, text="Alright sir", command=jogo_config)
    alright.pack(side=TOP)

# Janela principal do jogo...
def jogo_config():
    janela2.withdraw()
    janela3_open()
    global janela3
    randomizar_palavras()

    # Containers:
    container1 = Frame(janela3)
    container1["pady"] = 30
    container1.pack()
    container2 = Frame(janela3)
    container2.pack()
    container3 = Frame(janela3)
    container3.pack()
    container4 = Frame(janela3)
    container4.pack()

    # Widgets:
    choice = Label(container1,text="What's your guess?:")
    choice.pack(side=LEFT)

      # Espaço que o indivíduo escreve a letra
    global letter
    letter = Entry(container1)
    letter["width"] = 20
    letter.pack(side=LEFT)

      #Botão de tentativa
    enterbuttun = Button(container1, text="Try")
    enterbuttun.pack(side=BOTTOM)
    enterbuttun["command"] = verificar

      # Display das letras da palavra
    global forca
    forca = Label (container2, text=f"Palavra: " + " ".join(letras))
    forca.pack(side=RIGHT)

    texto = Label(container3, text="Your final answer?:")
    texto.pack(side=LEFT)
    texto["pady"] = 35
    texto["font"] = "arial, 7"

      # Espaço que o jogador escreve a palavra completa
    global theanswer
    theanswer = Entry(container3)
    theanswer["width"] = 20
    theanswer.pack(side=LEFT)
    theanswer["font"] = "arial, 7"

      # Botão de verificar resposta final
    enterbuttun2 = Button(container3, text="Sure?")
    enterbuttun2.pack(side=LEFT) 
    enterbuttun2["command"] = verificar
    enterbuttun2["font"] = "arial, 7"
    enterbuttun2["pady"] = 2

    texto1 = Label(container4, text="You must type your guess!")
    texto1.pack(side=LEFT)
    texto1["pady"] = 0
    texto1["font"] = "arial, 7"
    texto1["fg"] = "red"
    
# Verificar o que o jogador inseriu
def verificar():
    global letstry
    letstry = letter.get()
    global answer
    answer = resposta
    fullanswer = theanswer.get()
    letter.delete(0, END)   # Limpa a caixa de entrada da letra
    theanswer.delete(0,END)    # Limpa a caixa de entrada da resposta completa
    global letras
    global tentativas

    if letstry in resposta:
        for idx, letra in enumerate(resposta):  # Vê se a letra inserida está na resposta
            if letra == letstry:
                letras[idx] = letstry
        forca.config(text=f"Palavra: " + " ".join(letras))  # Edita do "_" para a letra 
    elif letstry not in answer:
        tentativas -= 1   # Reduz das tentativas
        print(f"mais {tentativas}")  # Informa quantas tentativas restantes tem
        if tentativas == 0:
            derrota()
    else:
        ()
    
    if fullanswer == answer:
        vitoria()
    else:
        if fullanswer not in answer:    
            derrota()
    
    
# Se acertar:
def vitoria():
    janela3.withdraw()
    janela5_open()
    global janela5

    # Containers:
    container1 = Frame(janela5)
    container1["pady"] = 30
    container1.pack()

    # Widgets: 
    texto1 = Label(container1, text="OH SHIT")
    texto1.pack(side=TOP)
    texto1["fg"] = "darkgreen"
    
    texto2 = Label(container1, text="You actually got it right!")
    texto2.pack()
    
    texto3 = Label(container1, text=":o")
    texto3.pack()

      # Botões:
    restart = Button(container1, text="Restart", command=start_jogo)
    restart.pack()
    botaosair = Button(container1, text="Quit", command=quit)
    botaosair.pack(side=BOTTOM)

# Se perder:
def derrota():
    janela3.withdraw()
    janela4_open()
    global janela4

    # Containers:
    container1 = Frame(janela4)
    container1["pady"] = 30
    container1.pack()

    # Widgets:
    texto4 = Label(container1, text="Uh-Oh!")
    texto4["fg"] = "darkred"
    texto4.pack(side=TOP)

    texto5 = Label(container1, text="Seems like you lost")
    texto5.pack()

    texto1 = Label (container1, text= f"The answer was: {resposta}")
    texto1.pack()

      # Botões:
    restart1 = Button(container1, text="Restart", command=restartfr)
    restart1.pack()
    botaosair = Button(container1, text="Quit", command=quit)
    botaosair.pack(side=BOTTOM)

def reiniciar1():
    janela4.withdraw()
def reiniciar2():
    janela5. withdraw()

def start_jogo():
    reiniciar2()
    abre_textos1()

def restartfr():
    reiniciar1()
    jogo_config()

# Inicia o jogo:  
abre_textos1()

quit()