from lab2b import *
import os
def menu():
    print("1. Skriv ut en existerande lista\n2. Lägg till ett föremål i listan\n3. Ta bort ett föremål ur listan\n4. Ändra ett föremål i listan\n5. Avsluta")

ls = create_shopping_list()
print("Välkommen till shoppinglistan, välj ett alternativ:")
while True:
    menu()
    choice = int(input(""))
    print()
    options = { 1: shopping_list,
                2: shopping_add,
                3: shopping_remove,
                4: shopping_edit,
                5: exit
    }
    os.system('clear')
    if choice == 5:
        print("Hej då!")
        options[5]()
    else:
        options[choice](ls)
    print()
