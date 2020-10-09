#!/usr/bin/python3

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
    
def binary_search(sorted_list, needle, comp_func=None):
    minst = 0
    högst = len(sorted_list)
    average = int(högst/2)
    #print(sorted_list[average])
    if sorted_list[average] == needle:
        return sorted_list[average]
    elif sorted_list[average] < needle:
        return binary_search(sorted_list[average:högst], needle, func)
    elif sorted_list[average] > needle:
        return binary_search(sorted_list[minst:average], needle, func)


def insertion_sort(lista, func):
    for i in range(1, len(lista)):
        if func(lista[i]) < func(lista[i-1]):
            temp = lista.pop(i)
            for j in range(0, len(lista)):
                if func(temp) < func(lista[j]):
                    lista.insert(j, temp)
                    break
            
                
                        
    
    
def main():
    # Linear Search
    a_list = [num for num in range(100)]
    # b = linear_search(a_list, -1)
    # c = linear_search(a_list, 16)
    # print(b, c, sep='\t')
    # imdb_list = [{'title': 'Professional Help', 'actress': 'Big Chungus', 'score': 2}, {'title': 'Raising an error', 'actress': 'Big Cobra', 'score': 5}, {'title': 'Raise your voice', 'actress': 'Hilary Duff', 'score': 10}]
    # chungus = linear_search(imdb_list, 'Big Cobra', func=lambda e: e['actress'])
    # ph =  linear_search(imdb_list, 'Professional Help', func=lambda e: e['title'])
    # not_found = linear_search(imdb_list, 'Something Else', func=lambda e: e['title'])
    # print(chungus, ph, not_found, sep='\n')
    
    # Binary Search
    #bs_res = binary_search(a_list, 70)
    #print('BS: ', bs_res)

    # Insertion Sort
    db = [
        ('j', 'g'), ('a', 'u'), ('k', 'l'), ('o', 'i'),
        ('b', 's'), ('@', '.'), ('p', 's'), ('o', 'e')
    ]
    print(db)
    insertion_sort(db, lambda e: e[0])
    print(db)
    
if __name__ == '__main__':
    main()

