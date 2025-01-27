import os
from colorama import init, Fore
import random

# Variaveis importantes, a resposta e tentativas, o display das letras. 
def randomizar_palavras():
    global tentativas
    tentativas = 8  # Tentativas totais que o jogador possui
    global palavras
    palavras = ['casa', 'abacate', 'flores', 'tangerina', 'verde', 'iluminação']  # Lista de palavras que podem ser a resposta
    global answer
    answer = random.choice(palavras)  # Randomiza as plavras dentro da lista 'palavras'
    global letras
    letras = ["_" for letra in answer]  # Substitui as letras por "_"
    global numeroLetras
    numeroLetras = len(answer)  # Conta quantas letras tem na 'answer'

# Limpa o terminal
def clear():
    os.system('clear')

# Menu inicial
def menu_intro():
    clear()  # Limpa o terminal

    ####################
    ## Visual do menu
    ####################
    print("")
    print(Fore.LIGHTWHITE_EX + "«-»«-»«-»«-»«-»«-»«-»«-»«-»«-»«-»«-»«-»«-»")
    print(Fore.GREEN + "         I welcome you, sir")
    print(Fore.WHITE + "     To my humbling little game:")
    print(Fore.RED + "            The Hangman!")
    print(Fore.LIGHTWHITE_EX + "«-»«-»«-»«-»«-»«-»«-»«-»«-»«-»«-»«-»«-»«-»")
    print("       Ready to lose, big guy? :p")
    firstchoice = input(" Y/N?: ")  # Jogador insere se quer jogar ou não

    # Se escolher y ou n
    if firstchoice == "y":
        are_you_sure()
    elif firstchoice == "n":
        quit

# Menu explicando como funciona o jogo
def are_you_sure():
    clear()  # Limpa terminal

    ################
    ## Layout da explicação
    ################
    print(Fore.WHITE + "─·─·─·─·─·─·─·─··─·─·─·─··─·─·─·─·─·─·─·─·─·─·─·─·")
    print(Fore.RED + "                HOW DOES IT WORK")
    print(Fore.WHITE + "All you gotta do is guess the word and or letters")
    print(Fore.LIGHTMAGENTA_EX + "            You got 8 tries, alright?")
    choice = input(Fore.WHITE + "          If so, type alright: ")
    
    # Se escrever "alright" certo ou errado
    if choice == "alright":
        randomizar_palavras()
        game()
    else:
        clear()  #limpa o terminal

        #####################
        ## Layout pra pagina de erro
        #####################
        print(Fore.WHITE + "«-»«-»«-»«-»«-»«-»«-»«-»«-»«-»«-»«-»«-»«-»«-»")
        print(Fore.WHITE + " Ops, seems like you don't know how to write")
        tryagain = input("Try again?(y/n): ")
        print(Fore.WHITE + "«-»«-»«-»«-»«-»«-»«-»«-»«-»«-»«-»«-»«-»«-»«-»")
        # Se o jogador vai querer continuar jogando ou não
        if tryagain == "y":
            are_you_sure()
        if tryagain == "n":
            quit
        else:
            quit

# Menu do jogo
def game():
    clear()  #limpa o terminal

    ######################
    ## Monta o layout do jogo
    ######################
    print(Fore.WHITE + "«-»«-»«-»«-»«-»«-»«-»«-»«-»«-»«-»«-»«-»«-»«-»«-»«-»«-»«-»«-»«-»«-»«-»«-»«-»")
    print(f"                    Your word got: {numeroLetras} letters!")  # Informa ao jogador quantas letras tem a palavra escolhida
    print(f"                          You got {tentativas} tries")  # Informa ao jogador quantas tentativas restam
    global forca
    forca = print(f'''                 _______
                |       |
                |       ⊥
                |
                |
                |
                |       ''' + " ".join(letras))  # Mostra visualmente a quantidade de letras, o tamanho da palavra
    print("")
    
    global wordchosen
    wordchosen = input("Choose a letter or the answer sweetie: ")  # Pede pro jogador escrever uma letra ou a palavra
    config_game()

# Configuração do jogo de acordo com a palavra/letra que o jogador escolheu
def config_game():
    global tentativas  # Chamou o variável
    
    if wordchosen == answer:  # Se acertar a resposta
        win()
    elif wordchosen in answer:  # Se tiver a letra na resposta
        for idx, letra in enumerate(answer):  # Vê onde a letra esta na resposta
            if letra == wordchosen:
                letras[idx] = wordchosen
        forca == print(f'''                 _______
                |       |
                |       ⊥
                |
                |
                |
                |       ''' + " ".join(letras))   # Edita o texto da forca
        game()  # Volta pro jogo
    elif wordchosen != answer:  # Se o que o jogador colocou não estiver na resposta
        if tentativas >= 1:
            clear()
            tentativas -=1
            print(f"You got {tentativas} tries left")  # Edita o texto sobre as tentativas, atualizando
            game()  # Volta pro jogo
        elif tentativas == 0:
            derrota()  # vai pra cena de derrota

# Layout caso o jogador use todas suas tentativas, e se quer continuar jogando, tentar de novo
def derrota():
    clear()  # Limpa o terminal
    ##################
    ## Layout da derrota pra quem zerar as chances
    ##################
    print(Fore.WHITE + "«-»«-»«-»«-»«-»«-»«-»«-»«-»«-»«-»«-»«-»«-»«-»")
    print(Fore.RED + "                  UH-OH")
    print(Fore.WHITE + "              You actually lost!!")
    print(f"Answer: {answer}")
    print(Fore.WHITE + "«-»«-»«-»«-»«-»«-»«-»«-»«-»«-»«-»«-»«-»«-»«-»")
    print("")
    tryagain = input("              Try again?[Y/N]: ")  # Pede pra pessoa escolher se quer jogar de novo/continuar
    # Caso jogador escolha "y" ou "n"
    if tryagain == 'y':
        recomecar()
    elif tryagain == 'n':
        quit()
    else:
        quit()


# Layout da cena de vitória e sua configuração, caso queira jogar de novo
def win():
    clear()  # Limpa o terminal
    
    ##############
    ## Layout da vitória pta quem vencer
    ##############
    print(Fore.WHITE + "«-»«-»«-»«-»«-»«-»«-»«-»«-»«-»«-»«-»«-»«-»«-»")
    print(Fore.GREEN + "                  OH MA GAH")
    print(Fore.WHITE + "              You actually won!!")
    print(f"Answer: {answer}")
    print(Fore.WHITE + "«-»«-»«-»«-»«-»«-»«-»«-»«-»«-»«-»«-»«-»«-»«-»")
    print("")
    restart = input("              Try again?[Y/N]: ")  # Pede pra pessoa escolher se quer jogar de novo
    # Caso jogador escolha "y" ou "n"
    if restart == 'y':
        recomecar()
    elif restart == 'no':
        quit()
    else:
        quit()

# Função pra rodar o jogo de novo
def recomecar():
    randomizar_palavras()
    menu_intro()

# Inicia o programa
menu_intro()