import os
from colorama import init, Fore

try:
    int(input("batata"))

except:
    print("Error, you must type a number! try again loser")

def clear():
    os.system('clear')

wishlist = []

def intro():
    clear()
    print(Fore.WHITE + "~¨~¨~¨~¨~¨~¨~¨~¨~¨~¨~¨~¨~¨~¨~¨~¨~¨~")
    print(Fore.LIGHTBLUE_EX + "          Welcome dear!")
    print(Fore.LIGHTWHITE_EX +"       What do you wish for?")

def menu_choices():
    print(Fore.WHITE + "-----------------------------------")
    print(Fore.LIGHTYELLOW_EX + "        Choose carefully!!")
    print(Fore.WHITE + "-----------------------------------")
    print()
    print("       1. Wanna add things?")
    print("       2. Perhaps, remove?")
    print("    3. Don't tell me you gave up!")
    print()
    choice = int(input(Fore.LIGHTMAGENTA_EX + "So...?: "))


    if choice == 1:
        add_items()
    elif choice == 2:
        remove_items()
    elif choice == 3:
        clean_items()
    



    
def add_items():
    clear()
    print(Fore.WHITE + "-----------------------------------")
    global whish
    whish = (input(Fore.LIGHTGREEN_EX + '''      So... What's gonna be?: 
            '''))
    wishlist.append(whish)
    clear()
    print("~¨~¨~¨~¨~¨~¨~¨~¨~¨~¨~¨~¨~¨~¨~¨~")
    print("   New item add: " + whish)
    print("~¨~¨~¨~¨~¨~¨~¨~¨~¨~¨~¨~¨~¨~¨~¨~")
    print(Fore.WHITE)
    print(wishlist)
    
    
    yesorno = int(input(Fore.GREEN + '''
Anything else? (1 for yes, 0 for no): '''))
    
    if yesorno == 1:
        print(intro(), menu_choices())
    elif yesorno == 0:
        clear()
        end()


def remove_items():
     clear()
     print(Fore.WHITE + "-----------------------------------")
     whish = (input(Fore.LIGHTGREEN_EX + '''      So... What's gonna be?: 
            '''))
     wishlist.remove(whish)
     clear()
     print("~¨~¨~¨~¨~¨~¨~¨~¨~¨~¨~¨~¨~¨~¨~¨~")
     print("     buh-bye: " + whish)
     print("~¨~¨~¨~¨~¨~¨~¨~¨~¨~¨~¨~¨~¨~¨~¨~")
     print(Fore.WHITE)
     print(wishlist)
    
     yesorno = int(input(Fore.GREEN + '''
Anything else? (1 for yes, 0 for no): '''))
    
     if yesorno == 1:
        print(intro(), menu_choices(), )
     elif yesorno == 0:
        clear()
        end()

def clean_items():
     clear()
     print()
     wishlist.clear()
     clear()
     print(Fore.RED + "~¨~¨~¨~¨~¨~¨~¨~¨~¨~¨~¨~¨~¨~¨~¨~")
     print("           Adios mf! " )
     print("~¨~¨~¨~¨~¨~¨~¨~¨~¨~¨~¨~¨~¨~¨~¨~")
     print(Fore.WHITE)
     

     yesorno = int(input(Fore.GREEN + '''
Wanna leave then? (1 for yes, 0 for no): '''))
    
     if yesorno == 0:
        print(intro(), menu_choices())
     elif yesorno == 1:
        clear()
        end()
        

def end():
    clear()
    print()
    print(Fore.WHITE + "~¨~¨~¨~¨~¨~¨~¨~¨~¨~¨~¨~¨~¨~¨~¨~")
    print(Fore.BLUE + " Thank you for stopping by <3")
    print(Fore.WHITE + "~¨~¨~¨~¨~¨~¨~¨~¨~¨~¨~¨~¨~¨~¨~¨~")
    print()



intro()
menu_choices()
end()

