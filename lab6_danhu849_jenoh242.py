#!/usr/bin/python3
import json

content = []
with open("data.json") as data:
	content = json.load(data)
people = [{'name': 'Pontus', 'age': 30},
		{'name': 'Sara', 'age': 29},
		{'name': 'Sara', 'age': 28},
		{'name': 'Sara', 'age': 27},
		{'name': 'Sara', 'age': 26},
		{'name': 'Sara', 'age': 25},
		{'name': 'Sara', 'age': 24},
		{'name': 'Sara', 'age': 23},
		{'name': 'Sara', 'age': 22},
		{'name': 'Sara', 'age': 21},
		{'name': 'Sara', 'age': 20},
		{'name': 'Xavier', 'age': 19}]

people2 = [{'name': 'Pontus', 'age': 30},
		{'name': 'Sara', 'age': 28},
		{'name': 'Sara', 'age': 27},
		{'name': 'Sara', 'age': 24},
		{'name': 'Sara', 'age': 26},
		{'name': 'Sara', 'age': 29},
		{'name': 'Sara', 'age': 23},
		{'name': 'Sara', 'age': 22},
		{'name': 'Sara', 'age': 25},
		{'name': 'Sara', 'age': 20},
		{'name': 'Sara', 'age': 21},
		{'name': 'Xavier', 'age': 19}]


# Linjärsökning 
def linear_search(lista, value, func=None):
    if func == None:
        result = [item for item in lista if item == value]
        return result[0] if len(result) > 0 else print("No element found")
    else:
        for item in lista:
            if func(item) == value:
                return item
        return None

# LINJÄRSÖKNING
# def linear_search(haystack, needle, filt=lambda e: " ".join([str(item[1]) for item in e.items()])):
# 	for straw in haystack:
# 		if str(needle).lower() in str(filt(straw)).lower():
# 			return straw

# BINARY SEARCH
def binary_search(sorted_list, needle, comp_func=None):
    minst = 0
    högst = len(sorted_list)
    average = int(högst/2)
    if comp_func == None:
        if sorted_list[average] == needle:
            return sorted_list[average]
        elif sorted_list[average] < needle:
            return binary_search(sorted_list[average:högst], needle)
        elif sorted_list[average] > needle:
            return binary_search(sorted_list[minst:average], needle)
    else:
        if comp_func(sorted_list[average]) == needle:
            return sorted_list[average]
        elif comp_func(sorted_list[average]) < needle:
            return binary_search(sorted_list[average:högst], needle, comp_func)
        elif comp_func(sorted_list[average]) > needle:
            return binary_search(sorted_list[minst:average], needle, comp_func)

# BINARY SEARCH
# def binary_search(haystack, needle, filt = None):
# 	if len(haystack) == 1:
# 		if haystack[0] == needle:
# 			return haystack[0]
# 		else:
# 			return None
# 	if not filt:
# 		for key in haystack[0].keys():
# 			awnser = binary_search(haystack, needle, lambda e: e[key])
# 			if awnser:
# 				return awnser
# 	else:
# 		middle = int(len(haystack)/2)
# 		needle = str(needle)
# 		middle_straw = str(filt(haystack[middle]))
# 		if needle == middle_straw:
# 			return haystack[middle]
# 		elif needle > middle_straw:
# 			return binary_search(haystack[:middle], needle, filt)
# 		elif needle < middle_straw:
# 			return binary_search(haystack[middle:], needle, filt)

        
def insertion_sort(lista, func):
    for i in range(1, len(lista)):
        if func(lista[i]) < func(lista[i-1]):
            temp = lista.pop(i)
            for j in range(0, len(lista)):
                if func(temp) < func(lista[j]):
                    lista.insert(j, temp)
                    break

def quicksort(lista, func):
    if len(lista) <= 1:
        return lista
    else:
        pivot = func(lista[int(len(lista)/2)])
        #print("pivot: ", pivot)
        #print("LISTA: ", lista)
        pivot_index = int(len(lista)/2)
        left_lista = []
        right_lista = []
        for i in range(0, pivot_index):
            if func(lista[i]) < pivot:
                left_lista.append(lista[i])
            else:
                right_lista.append(lista[i])
        for j in range(pivot_index + 1, len(lista)):
            if func(lista[j]) < pivot:
                left_lista.append(lista[j])
            else:
                right_lista.append(lista[j])
        #print('left lista: ', left_lista)
        #print('right lista ', right_lista)
        return quicksort(left_lista, func) + quicksort([lista[int(len(lista)/2)]], func) + quicksort(right_lista, func)


def main():
    # Linear Search
    a_list = [num for num in range(100)]
    tupel_list = [(num%5==0, num * 2 + 1) for num in range(200,250)]
    b = linear_search(a_list, -1)
    c = linear_search(a_list, 16)
    print(b, c, sep='\t')
    imdb_list = [{'title': 'Professional Help', 'actress': 'Big Chungus', 'score': 2}, {'title': 'Raising an error', 'actress': 'Big Cobra', 'score': 5}, {'title': 'Raise your voice', 'actress': 'Hilary Duff', 'score': 10}]
    chungus = linear_search(imdb_list, 'Big Cobra', func=lambda e: e['actress'])
    ph =  linear_search(imdb_list, 'Professional Help', func=lambda e: e['title'])
    not_found = linear_search(imdb_list, 'Something Else', func=lambda e: e['title'])
    print(chungus, ph, not_found, sep='\n')
    print(linear_search(content, 9000, func = lambda e: e['lulz_had']))

    # Binary Search
    stl = quicksort(tupel_list, lambda e: e[1])
    print(stl)
    bs_tupel = binary_search(stl, 449, lambda e: e[1])
    bs_res = binary_search(a_list, 70)
    print('BS: ', bs_res)
    print(bs_tupel)

    # Insertion Sort
    db = [
        ('j', 'g'), ('a', 'u'), ('k', 'l'), ('o', 'i'),
        ('b', 's'), ('@', '.'), ('p', 's'), ('o', 'e')
    ]
    print(db)
    insertion_sort(db, lambda e: e[0])
    print('Sorted by first element: ', db)
    insertion_sort(db, lambda e: e[1])
    print('Sorted by second element: ', db)
    print(insertion_sort(people2, lambda e: e['age']))

    
    # Quicksort
    sorted_db = quicksort(db, lambda e: e[0])
    print('Quicksorted db: ', sorted_db)

if __name__ == '__main__':
    main()

