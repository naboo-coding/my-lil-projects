import os
from colorama import Fore

tasks = []  # Cria a lista para as tasks

def limpa_terminal():  # Auto explicativo
    os.system('clear')

def tchau():  # Função de dar tchau
    print("\nOkay, see you around \nBuh-bye then!!")
    quit()  # sai do programa
    
def display_tasks():  # Para não ter que repetir o código toda vez que quiser mostrar as tasks
    print(Fore.CYAN + f"You have {len(tasks)} things to do.")
    if len(tasks) == 0:  # Se não tiver nada ainda na lista
        print("")
    else:
        print(Fore.WHITE + "They are:\n")
        
    for task in tasks:  # Para cada task na lista das tasks faça isso:
        print(Fore.WHITE + f"→ {task} \n")

####              ####
##                  ##
##   MENU INICIAL   ##
##                  ##
####              ####
def inicial():
    limpa_terminal()  
    ###                                                                   ###
    # Recebe o usuario e vê se ele quer adicionar ou ver sua lista de tasks #
    ###                                                                   ###
    print("Hello, welcome.\n")
    display_tasks()
    choice = input(Fore.WHITE + "Would you like to add anything?[Y/N]:")

    if choice.lower() in ['y', 'yes']:  # Capta a informção dada pelo usuario e deixa em letra minúscula se ele digitar y
        add_task()

    elif choice.lower() in ['n', 'no']:  # Capta a informção dada pelo usuario e deixa em letra minúscula se ele digitar n
        tchau()

    else:  # Pra caso alguem digite algo nada a ver
        print("\nSorry, didn't get that. Try again.")
        again = input("Okay?")

        if again.lower() in ['okay', 'ok']:
            inicial()
        else:  # Se mesmo assim a pessoa quiser avacalhar
            tchau()

####                       ####
##                           ##
## PERGUNTA E ADICIONA TASKS ##
##                           ##
####                       ####
def add_task():
    limpa_terminal()  # Limpa o terminal

    ###                                    ###
    # Pergunta o que a pessoa quer adicionar #
    ###                                    ###
    display_tasks()
    addingTask = input(Fore.WHITE + "What would your task be?: ")
    
    if addingTask in ['nothing', '']:  # Se a pessoa não quiser adicionar nada
        print("\nOps, it's quite hard adding absolute nothing")
        tchau()

    elif addingTask not in ['nothing', '']:  # Se realmente for adicionar algo
        ##                                                ##
        # Adiciona na lista e verifica se quer algo a mais #
        ##                                                ##
        print("Good luck with" + Fore.RED + f" {addingTask}\n")
        tasks.append(addingTask)
        display_tasks()
        print(Fore.WHITE + "\nWould you like adding anything else?")
        yesorno = input("[Y/N]: ")

        if yesorno.lower() in ['y', 'yes']:  # Se sim
            add_task()
        elif yesorno.lower() in ['n', 'no']:  # Se não quiser adicionar
            seetasks = input("Would you like to see your tasks then?[Y/N]: ") # Confere se então a pessoa não quer ver as tasks
            if seetasks.lower() in ['y', 'yes']:  # Se quiser ver as tasks
                show_tasks()
            else:
                tchau()

####                      ###
##                         ## 
## MOSTRA AS TASKS QUE TEM ##
##  e se quer adicionar    ##
#     ou remover algo      ##
####                      ###
def show_tasks():
    limpa_terminal() # Limpa o terminal
    ###                          ###
    # Display do que tem pra fazer #
    ###                          ###
    display_tasks()
    remove = input("\nWould you like to remove or add any of them?")  # Pergunta se quer remover ou adicionar mais coisa

    if remove.lower() in ['remove']:  # Se quiser remover 
        remove_task()
    elif remove.lower() in ['add']:  # Se quiser adicionar
        add_task()
    else:  # Qualquer outra coisa que não seja y ou yes, cansei de fazer ifs
        tchau()

####                        ####
##                            ##
## REMOVE AS TASKS ESCOLHIDAS ##
##                            ##
####                        ####
def remove_task():
    limpa_terminal()  # Limpa o terminal 

    ###                                     ###
    # Apresenta as tasks para serem removidas #
    ###                                     ###
    display_tasks()
    print("\nSo... Which one do you want to remove?")
    choice = input("")
    tasks.remove(choice)  # Remove a task escolhida

    ###                                       ###
    # Pergunta se quer deletar mais alguma coisa#
    ###                                       ###
    print("All done, any other, if so which?")
    removeoutra = input("")
    
    if removeoutra not in tasks:  # Se o que for digitado não estiver na lista
        show_tasks()  # Mostra as tasks
    else:
        tasks.remove(removeoutra)  # Tira a task escolhida da lista
        while len(tasks) > 0:  # Enquanto tiver tasks na lista faça:
            print("All done, any other task, if so, which?")
            removeoutra = input("")
            if removeoutra not in tasks:  # se o que for digitado não estiver na lista
                seetasks = input("Would you like to see your tasks then?[Y/N]: ") # Confere se então a pessoa não quer ver as tasks
                if seetasks.lower() in ['y', 'yes']:  # Se quiser ver as tasks
                    show_tasks()
                else:
                    tchau()
            
inicial()