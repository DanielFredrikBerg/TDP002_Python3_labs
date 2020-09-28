#create new shopping list
def create_shopping_list():
    s_list = ["Kurslitteratur", "Anteckningsblock","Penna"]
    return s_list

#list items from shopping list
def shopping_list(s_list):
    p = 0
    for i in s_list:
        p += 1
        print(str(p) + ". " + i)

#add to shopping list
def shopping_add(s_list):
    s_list.append(input("Vad ska läggas till i listan? "))

#remove from shopping list
def shopping_remove(s_list):
    del s_list[int(input("Vilken sak ska du ta bort ur listan? "))-1]

#edit item in list
def shopping_edit(s_list):
    oldItemPos = int(input("Vilken sak vill du ändra på? ")) - 1
    newItem = input('Vad ska det stå istället för "' + s_list[oldItemPos] + '"? ')
    s_list[oldItemPos] = newItem
