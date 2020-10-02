#!/usr/bin/env python3
import os

#jenoh242 & danhu849, 2020-10-02

def main():
	while True:
		try:
			print("##########################################################")
			print("#Skriv 'a'-'h' för en uppgift.                           #")
			print("#Skriv 'exit', 'quit' eller 'q' för att avsluta.         #")
			print("##########################################################")
			choice = input("\n#Uppgift 5")
			print()
			if choice.lower() in ["exit", "quit", "q"]:
				break
			elif choice.lower() not in [chr(i) for i in range(97, 105)]:
				print("Inte en uppgift!")
			else:
				eval("assignment_" + choice.lower() + "()")
				print()
		except Exception as e:
			print(e)

##########assignments start here##########

#5a
#Tar en funktion och ett tal, och kallar funktionen med talet.
def somefunc(func, tal):
	return func(tal)

def assignment_a():
	summa = lambda x: x + summa(x-1) if (x > 0) else 0
	prod = lambda x: x * prod(x-1) if (x > 1) else 1
	add = int(input("Summera up till vilket tal?"))
	print("Summan av alla tal från 0 till ", add,":\n", somefunc(summa, add), "\n")
	times = int(input("Multiplicera upp till vilket tal?"))
	print("Produkten av alla tal från 1 till ", times,":\n", somefunc(prod,times))

#5b
#För varje person, kolla om söksträngen är finns i värdet av det angivna fältet
#Returnerar persons uppgifter om så är fallet.
def search_db(db, search_field, search_string):
	search_results = []
	for pers in db:
		if  search_string.lower() in pers[search_field].lower():
			search_results.append(pers)
	return search_results

def assignment_b():
	db = [
	{'name': 'Jakob', 'position': 'assistant'},
	{'name': 'Åke', 'position': 'assistant'},
	{'name': 'Ola', 'position': 'examiner'},
	{'name': 'Henrik', 'position': 'assistant'}
	]
	print("Databasen:\n", db, "\n")
	field = input("Vilket fält vill du söka på?\n")
	string = input("Vilket ord vill du söka på?\n")
	print("Svar på sökning: ", search_db(db, field, string))

#5c
#Använder "__contains__" för att kolla om ordert finns i listan.
def contains(word, haystack):
	return haystack.__contains__(word)

#Använder en "list comprehension" som fylls med instancer av det funna ordet.
#Om listan innehåller något, returnera "True".
def contains2(word, haystack):
	found = [oword for oword in haystack if oword == word]
	return bool(found)

#Samma som ovan fast ett lambda uttryck.
contains3 = lambda word, haystack: bool([oword for oword in haystack if oword == word])

def assignment_c():
	haystack = 'Can you find the needle in this haystack?'.split()
	print('Finns "needle" i ', haystack, "?\n")
	print("----------------------------------------------------------")
	print('|Med "__contains__"                               |' , contains('needle', haystack), "|")
	print("|--------------------------------------------------------|")
	print('|Med "list comprehension"                         |' , contains2('needle', haystack), "|")
	print("|--------------------------------------------------------|")
	print('|Med "List comprehension", fast i lambda funktion |' , contains3('needle', haystack), "|")
	print("----------------------------------------------------------")

#5d
def command_pwd():
	print(os.getcwd())

#Tar in en sökväg till en katalog, och listar innehållet för.
#Om inget anges används katalogen användaren står i.
def command_ls(path = '.'):
	for file_name in os.listdir(path):
		print(file_name)

#Hittar sökvägen till nuvarande katalog, och skriver ut den.
def command_cd(path = '.'):
	os.chdir(path)

#Öppnar en fil, och skriver ut innehållet.
def command_cat(path):
	if path:
		with open(path, 'r') as content:
			print(content.read())
	else:
		print('Please add args for cat')

def assignment_d():
	print('Kommandon: pwd, ls, cd, cat')
	print('Skriv "exit", "quit" eller "q" för att avsluta.')
	while(True):
		try:
			command = input("command> ")
			command = command.split(' ')
			if command[0].lower() in ["q", "exit", "quit"]:
				break
			elif len(command) > 1:
				eval("command_" + command[0] + '("' + command[1] + '")')
			else:
				eval("command_" + command[0] + '()')
		except Exception:
			print('No such command')

#5e
stars = lambda n : '*' * n

#Genererar en n lång lista med hjälp av en funktion.
generate_list = lambda func, n: [func(variable) for variable in range(1, n+1)]

def assignment_e():
	ammount = int(input("Hur många stjärnor? "))
	print(generate_list(stars, ammount))

#5f
add = lambda x, y: x + y

#Skapar en "förifylld" funktion.
def partial(func, condition):
	return lambda value: func(condition, value)

def assignment_f():
	print("Addera två siffror.")
	num = int(input("skriv det första nummret: "))
	add_num= partial(add, num)
	num = int(input("Skriv det andra nummret: "))
	print(add_num(num))

#5g
m_5 = lambda x: x * 5
a_10 = lambda x: x + 10

#Skapar en funktion av en funktion i en funktion.
def compose(F_a, F_b):
	return lambda x: F_a(F_b(x))
	
def assignment_g():
	x = int(input("f(x) = (x * 5) + 10\nSkriv nummer för x: "))
	composition = compose(a_10, m_5)
	print(composition(x))

#5h
#Skapar en ny funktion av två funktioner.
def make_filter_map_test(filt_func, pow_func):
	def new_func(lista):
		ue_filter_func = partial(filter, filt_func)
		pow_function = partial(map, pow_func)
		multiplied_func = compose(pow_function, ue_filter_func)
		return list(multiplied_func(lista))
	return new_func

def assignment_h():
	process = make_filter_map_test(lambda x: x % 2 == 1, lambda x: x * x)
	print("Skapar en lista där varje position är x * x om x är ojämt, och x går från noll till n.")
	n = int(input("Skriv nummer för n: "))
	print(process(range(n+1)), sep ="\t")

if __name__ == "__main__":
	main()
