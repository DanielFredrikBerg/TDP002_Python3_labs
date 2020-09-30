#!/usr/bin/env python3
import math
import os, sys

#Uppgift 1a
#print("Summan av alla naturliga tal mellan 0 och 512 är: ", sum(range(0,512 + 1, 1)), end='\n')

sum = 0
for nat_number in range(0, 512 + 1, 1):
    sum += nat_number
    #print(nat_number, end='\n')
#print("Summan av alla naturliga tal mellan 0 och 512 är: ", sum)


#Uppgift 1b
prod = 1
for mult_number in range(1, 512 + 1, 1):
    prod = prod * mult_number
#print("Produkten av alla tal mellan 1 och 512 är: ", prod, end='\n')

#LAB5
#5a
#lamda funktion av ovan:
def somefunc(func, tal):
    return func(tal)

summa = lambda x: x + summa(x-1) if (x > 0) else 0
prod = lambda x: x * prod(x-1) if (x > 1) else 1
print(somefunc(summa,512))
print(somefunc(prod,512))

#5b
db = [
{'name': 'Jakob', 'position': 'assistant'},
{'name': 'Åke', 'position': 'assistant'},
{'name': 'Ola', 'position': 'examiner'},
{'name': 'Henrik', 'position': 'assistant'}
]
def search_db(db, search_field, search_string):
    search_results = []
    for dic in db:
        if dic[search_field] == search_string:
            search_results.append(dic)
    return search_results
print(search_db(db, 'position', 'examiner'))

#5c
haystack = 'Can you find the needle in this haystack?'.split()
def contains(word, haystack):
    return haystack.__contains__(word)
print(contains('needle', haystack))

def contains2(word, haystack):
    found = [oword for oword in haystack if oword == word]
    return bool(found)
print(contains2('needle', haystack))

contains3 = lambda word, haystack: bool([oword for oword in haystack if oword == word])
print(contains3('needle', haystack))

#5d
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

#should be True to work
while(False):
    try:
        command = input("command> ")
        command = command.split(' ')
        if len(command) > 1:
            eval(command[0] + '("' + command[1] + '")')
        else:
            eval(command[0] + '()')

    except Exception:
        print('No such command')
    
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
#lista = [num for num in range(10)]

#filt_func = lambda x: x % 2 == 1
#pow_func = lambda x: x * x

def make_filter_map_test(filt_func, pow_func):
    def new_func(lista):
        ue_filter_func = partial(filter, filt_func)
        pow_function = partial(map, pow_func)
        multiplied_func = compose(pow_function, ue_filter_func)
        return list(multiplied_func(lista))
    return new_func

#print(list(ue_filter_func(lista)))
#print(list(multiplied_func(lista)))

process = make_filter_map_test(lambda x: x % 2 == 1, lambda x: x * x)
print(process(range(10)), 'test', sep='\t')



def make_filter_map(filt_func, map_func):
    l = [i for i in range(10)]
    print(filter(filt_func, l))

make_filter_map(lambda x: x % 2 == 1, lambda x: x * x)


def make_filter_map2(filt_func, map_func):
    return lambda lista: [map_func(item) for item in lista if filt_func(item)]

c_answer = make_filter_map(lambda x: x % 2 == 1, lambda x: x * x)
print(c_answer(range(10)), 'right answer', sep='\t')





#Uppgift 1c, minsta positiva talet delbart med alla heltal 1 till och med 13
num = 0
complete = True
while(complete):
    num += 1
    for mod in range(2, 13 + 1):
        # Om num inte är jämnt delbart med mod gå till nästa tal
        if num % mod != 0:
            break
        #När alla varianter av modulus utförts break:a while-loopen
        if mod == 13:
            complete = False   
#print("Minsta positiva heltalet delbart med alla heltal 1 till och med 13:", num, end='\n')


#Uppgift 1d, summera alla primtal under 1000
n = 1000
sum = 0
for num in range(2, n):
    for mod in range(2, num - 1):
        if num % mod == 0:
            break
    else:
        sum += num
#print('Summan är ' + str(sum))
