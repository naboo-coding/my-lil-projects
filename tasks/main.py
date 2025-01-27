from banco import *
from colorama import Fore
import os
from getpass import getpass
import subprocess
from docx import Document

def limpa_terminal():  # Acho bem autoexplicativo
    os.system("clear")

def tchau():  # Para não ficar escrevendo tanto toda hora :D
    print(f"\nGuess you got nothing else here then, \nSee you soon {username}!")

########                  ########
##                              ##
##  PRIMEIRO CONTATO COM O USER ##
##                              ##
########                  ########
def welcome():
    limpa_terminal()  # Limpa o terminal

    ###                      ###
    #  Mensagem de boas vindas #
    # pergunta quem é o usuario#
    ###                      ###
    print(Fore.CYAN + "Welcome, wlcome!")
    print(Fore.WHITE + "May i know your name?\n")
    global username
    username = input("Name: ").strip()  # Esse .strip() retira os vão em branco, ou seja, não vale input vazio, teoricamente

    if username == "":  # Se só der enter e não escrever nada
        quit()

    global findname
    findname = session.query(Usuario).filter_by(nome=username).first()  # Procura se o input do user existe no bd

    if findname:
        ##                                       ##
        # Informando que o usuário foi encontrado #
        ##                                       ##
        print(f"\nSeems like i found you, welcome back {username}")
        print("Would you like to see what you have?")
        see = input("[Y/N]: ").strip()

        if see.lower() in ['y', 'yes', 'ye']:  # Se a pessoa quiser vai levar ao menu
            menu()
        else:  # Se não, o programa vai parar de rodar
            tchau()

    else:
        ##                                             ##
        # Informa que não conseguiu encontrar o usuario #
        ##                                             ##
        print(f"\nOps, couldn't find you \nAre you sure you've been here before {username}?")
        haveuser = input("[Y/N]: ").strip()

        if haveuser.lower() in ['y', 'yes', 'ye']:  # Se o usuário tem certeza, é levado pro janela inicial
            welcome()
        else:
            new_user()  # Leva pra função que cria um novo usuário


########             ########
##                         ##
##    CRIA NOVO USUÁRIO    ##
##                         ##
########             ########
def new_user():
    limpa_terminal()  # Limpa terminal

    ###                                                           ###
    # Da mais uma boa vinda pro novo usuário e pede info necessária #
    ###                                                           ###
    print("Oh my, oh my, first time here " + Fore.RED + f"{username}" + Fore.WHITE + "? \nShall we create an account for you?") 
    name = input("\nWhat's you nickname gonna be?: ").strip()
    senha = input("\nAnd what about your password?: ").strip()

    if name == "" or senha == "":  # Caso só clique enter
        quit()

    else:
        global newuser
        newuser = Usuario(nome=name, senha=senha)  # Adiciona o usuário previamente
        session.add(newuser)  # Adiciona de fato o usuário na db
        session.commit()  # Salva na db

        ##                                                   ##
        # Mais uma boa vinda, pergunta se quer adicionar algo #
        ##                                                   ##
        print(f"\nI'm so happy, welcome" + Fore.GREEN + f"{name}" + Fore.WHITE + ", you're now part os a cult!!")
        print("Now, would you like to add something?")
        answer = input("[Y/N]: ").strip()

        if answer.lower() in ['y', 'yes', 'ye']:
            quit()
            pass # Tem que criar a função que leva a parte de edição das tarefas e notas
        else:
            tchau()  # Da tchauzinho pra titia <3

########         ########
##                     ##
##    MENU PRINCIPAL   ##
##                     ##
########         ########
def menu():
    global nomes
    nomes = (username or newuser)  # Pega o nome do user
    global password
    password = getpass("Before all, what would your password be?: ").strip()  # Getpass codifica a senha para não conseguirem ver, legal, ele cancela o echo, o mostrar do input

    checkuser()

########          ########
##                      ##
##   CHECAGEM DO USER   ##
##                      ##
########          ########
def checkuser():
    usuariocheck = session.query(Usuario). filter_by(nome=nomes, senha=password).first() # Confere se o nome e a senha batem com a db

    if usuariocheck:
        limpa_terminal() # Limpa o terminal
        # User x é o dono? então dale o que ele tem!
        tasks = session.query(Task).filter_by(user=nomes).all()  # Pega todas as tasks que tem o nome do user
        notes = session.query(Note).filter_by(user=nomes).all()  # Pega todas as notes que tem o nome do ueser

        print(Fore.LIGHTCYAN_EX + f"Nice to see you back, " + Fore.BLUE + f"{nomes}")
        print(Fore.WHITE + f"\nYou have a total of {len(tasks)} tasks and {len(notes)} notes.")

        display_tasks()  # Mostra as tasks
        display_notes()  # Mostra as notas

        ##                                  ##
        # Se gostaria de editar alguma coisa #
        ##                                  ##        
        print("\nWould you like to edit something?")
        editsmth = input("Is it gonna be the notes or the tasks?[N/T] \nIf you don't want to edit anyting, just write 'nothing': ").strip()

        if editsmth.lower() in ['n', 'notes']:  # Para editar as notas:
            edit_notes()

        elif editsmth.lower() in ['t', 'tasks']:  # Para editar as tasks:
            edit_tasks()

        else:
            tchau()

    else:  # Se a pessoa digitar a senha errada
        print("\nOps, are you sure that was your password?")
        maybe = input("[Y/N]: ").strip()

        if maybe.lower() in ['y', 'yes', 'ye']:  # Da mais uma chance
            print(f"Try again then {nomes}")
            menu()

        else:  # Se não, tchau tchau
            print("\nSorry, for secure resons, \nI can't ask you to create a new password<3")
            print("Just to show how much i care for my people ;p")
            tchau()

########                          ########
##                                      ##
## O QUE O USER QUER FAZER COM AS TASKS ##
##                                      ##
########                          ########
def edit_tasks():
    limpa_terminal()  # Limpa terminal
    display_tasks()  # Mostra as tasks

    whatedit = input("Remove, add, update or quit?[R/A/U/Q]: ")  # Pergunta as opções

    if whatedit.lower() in ['r', 'remove']:  # Caso o user queira remover algo
        taskremove = input("What task would you like to remove?: ").strip()

        task = session.query(Task).filter_by(todo=taskremove).first()  # Procura esse algo na db
        session.delete(task)  # Deleta
        session.commit()  # Salva

        print(f"{taskremove} went buh-bye")  # Avisa que a task foi removida
        display_tasks()  # Mostra as tasks

    elif whatedit.lower() in ['a', 'add']:  # Caso o user queira adicionar algo
        taskadd = input("What task would you like to add?: ").strip()

        task = Task(todo=taskadd, user=nomes, done=False)  # Adiciona a task previamente
        session.add(task)  # Adiciona de fato a task na db
        session.commit()  #Salva

        print(f"{taskadd} is now in your tasks!, check it out")  # Avisa que foi criada a task
        display_tasks()  # Mostra as tasks

    elif whatedit.lower() in ['u', 'update']:  # Caso o user queira atualizar o estado da task
        taskupdate = input("What task did you finish?: ").strip()

        task = session.query(Task).filter_by(todo=taskupdate).first()  # Procura a task na db
        task.is_done = not task.is_done  # Muda o estado da task para o contrário do atual
        session.commit()  # Salva

        print(f"{taskupdate} was updated")  # Informa
        display_tasks()  # Mostra as tasks

    else:
        tchau() 


########                          ########
##                                      ##
## O QUE O USER QUER FAZER COM AS NOTAS ##
##                                      ##
########                          ########
def edit_notes():
    limpa_terminal()  # Limpa o terminal
    display_notes()  # Mostra as notas

    ###                            ###
    # Pergunta o que o user gostaria #
    ###                            ###
    print("Would you like to remove, add, open an existing note, or quit?")
    whatwant = input("[R/A/O/Q]: ").strip()


    if whatwant.lower() in ['r', 'remove']: # Se a pessoa quiser deletar alguma nota
        noteremove = input("What note would you like to remove?: ").strip()

        note = session.query(Note).filter_by(noteName=noteremove).first()  # Procura pela nota
        session.delete(note)  # Apaga a nota
        session.commit()  # Salva a ação

        print(f"{noteremove} went buh-bye")  # Informa o user
        display_notes()  # Mostra as notas

    elif whatwant.lower() in ['a', 'add']:  # Se quiser adicionar alguma nota 
        new_nota()  # Leva pras config e adiciona a nota

    elif whatwant.lower() in ['o', 'open']:  # Se quiser apenas abrir uma nota
        abred_docx()  # Leva pra abir uma nota
    
    else: 
        quit()



########                 ########
###!                         !###
### DISPLAY DAS TASKS E NOTAS ###
###!                         !###
########                  ########
def display_tasks():
    tasks = session.query(Task).filter_by(user=nomes).all()  # Pega todas as tasks que tem o nome do user
    print("\nYour tasks are:")  # Se for maior que 0, printa
    
    if len(tasks) > 0:  # Confirma se o tanto de tasks é mais que 0
        for task in tasks:  # Para cada task faça: 
            print(f"→ {task.todo}" + f"     Are they donne?: {task.is_done}")  

    else:
        print(Fore.LIGHTRED_EX +"No tasks were add yet" + Fore.RESET)

def display_notes():
    notes = session.query(Note).filter_by(user=nomes).all()  # Pega todas as notes que tem o nome do ueser
    print("\nAnd your notes are:")  # Se for maior que 0, printa

    if len(notes) > 0:  # Confirma se o tanto de notas é mais que 0
        for note in notes:  # Para cada nota em notas faça:
            print(f"→ {note.noteName}")

    else:
        print(Fore.LIGHTRED_EX + "No notes were add yet" + Fore.RESET)

       
########                            ########
##                                        ##
## CONFIGURAÇÕES PARA ABRIR O DOC EXIGIDO ##
##                                        ##
########                            ########
def abred_docx():
    title = input("What note would you like to open?: ").strip()

    notecheck = session.query(Note).filter_by(noteName=title).first()  # Procura pela nota exigida
    caminho_arquivo = os.path.join("e/notes", f"{title}.docx")  # Acha o caminho até ela
    
    if notecheck:  # Se a nota existir:
        subprocess.run(["libreoffice", "--writer", caminho_arquivo])  # Abre a nota para poder editarem

    else:  # Se não existir:
        print("I couldn't quite find that note in my memory, sorry :(")  # Informa que não conseguiu achar
        create = input("Would you like to create one?[Y/N]: ").strip()  # Pergunta se gostaria de criar
        
        if create.lower() in ['y', 'yes', 'ye']:  # Se sim
            new_nota()  # Leva pra área de criação da nota
            print(f"{title} was added to your notes!")  # E informa que a ação foi realizada
            
        display_notes()  # Mostra as notas


########                            ########
##                                        ##
## CONFIGURAÇÕES PARA CRIAR O DOC EXIGIDO ##
##                                        ##
########                            ########
def new_nota():
    noteadd = input("What name would you like to give you new note?: ")  # Pergunta o nome da nota que gostaria adicionar
    
    
    os.makedirs("e/notes", exist_ok=True)  # Cria a pasta notes, para poder arquivar o documento
    caminho_arquivo = os.path.join("e/notes", f"{noteadd}.docx")  # Acha o caminho até o documento

    doc = Document()  # Cria o docuemnto
    doc.add_paragraph(nomes + "Ohohoh I'm so excited! What're you gonna write today?")  # Mensagenzinha de boas-vindas nas notas
    doc.save(caminho_arquivo)  # Salva o docuemento, podendo ver ele na pasta notes

    
    with open(caminho_arquivo, 'rb') as f:  # Abre o caminho para o "caminho_arquivo" e fala que é pra ler esse arquivo em read binary(rb), vulgo em binário. O with garate que o código se fecha.
        conteudo_blob = f.read()  # Aqui lê todos os dados presentes no arquivo em bytes mesmo

    novanote = Note(noteName=noteadd, note=conteudo_blob, user=nomes)  # Adiciona provisóriamente no bd as informações dada pelo usuário
    session.add(novanote)  # Adiciona de fato
    session.commit()  # Salva no bd
    print(f"{noteadd} is now in your notes!")  # Avisa o user
    

    if input("Open note? (y/n): ").lower() == 'y':  # Se o user vai realmente querer abrir o documento criado
        subprocess.run(["libreoffice", "--writer", caminho_arquivo])  # Chama o docuemnto criado para ser editado

    else: 
        checkuser()


# Inicia a rodagem do código
welcome()  