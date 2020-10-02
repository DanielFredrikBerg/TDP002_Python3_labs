import os

def main():
	assignments = []
			
	while True:
		choice = input("Vilken funktion vill du köra? \n 5a : 1 \n 5b : 2 \n 3  : 5c \n 5d : 4 \n 5e : 5 \n 5f : 6 \n 5h : 7")
		eval(assignments[choice])

	

#####################################################################################################
#5a
def a():
	summa = lambda x: x + summa(x-1) if (x > 0) else 0
	prod = lambda x: x * prod(x-1) if (x > 1) else 1
	print(somefunc(summa,512))
	print(somefunc(prod,512))
def somefunc(func, tal):
	return func(tal)
#5b
def b():
	db = [
	{'name': 'Jakob', 'position': 'assistant'},
	{'name': 'Åke', 'position': 'assistant'},
	{'name': 'Ola', 'position': 'examiner'},
	{'name': 'Henrik', 'position': 'assistant'}
	]
	print(search_db(db, 'position', 'examiner'))
def search_db(db, search_field, search_string):
	search_results = []
	for dic in db:
		if dic[search_field] == search_string:
			search_results.append(dic)
	return search_results
#5c
def c():
	haystack = 'Can you find the needle in this haystack?'.split()
	print(contains('needle', haystack))
	print(contains2('needle', haystack))
	print(contains3('needle', haystack))

def contains(word, haystack):
	return haystack.__contains__(word)

def contains2(word, haystack):
	found = [oword for oword in haystack if oword == word]
	return bool(found)

contains3 = lambda word, haystack: bool([oword for oword in haystack if oword == word])

#5d
def d():
	while(True):
		try:
			command = input("command> ")
			command = command.split(' ')
			if len(command) > 1:
				eval(command[0] + '("' + command[1] + '")')
			elif command[0] == "q":
				break
			else:
				eval(command[0] + '()')
		except Exception:
			print('No such command')
		
def cat_func(path):
	with open('path', 'r') as content:
		return content
def pwd():
	print(os.getcwd())
def ls(path = '.'):
	for file_name in os.listdir(path):
		print(file_name)
def cd(path = '.'):
	os.chdir(path)
def cat(path):
	if path:
		with open(path, 'r') as content:
			print(content.read())
	else:
		print('Please add args for cat')


#5e
def stars(n): return '*' * n
gen_list = lambda func, integer: [func(variable) for variable in range(1, integer +1)]
print(gen_list(stars, 3))

#5f
add = lambda x, y: x + y

def partial(func, condition):
	return lambda value: func(condition, value)

add_five = partial(add, 5)
print(add_five(3))

#5g
m_5 = lambda x: x * 5
a_10 = lambda x: x + 10

def compose(F_a, F_b):
	return lambda x: F_a(F_b(x))
	
composition = compose(a_10, m_5)
print(composition(3))

#5h

def make_filter_map_test(filt_func, pow_func):
	def new_func(lista):
		ue_filter_func = partial(filter, filt_func)
		pow_function = partial(map, pow_func)
		multiplied_func = compose(pow_function, ue_filter_func)
		return list(multiplied_func(lista))
	return new_func

def make_filter_map_test2(filt_func, pow_func): return lambda l: list(compose(partial(filter, filt_func), partial(map, pow_func)))

process = make_filter_map_test(lambda x: x % 2 == 1, lambda x: x * x)
print(process(range(10)), 'test', sep='\t')
