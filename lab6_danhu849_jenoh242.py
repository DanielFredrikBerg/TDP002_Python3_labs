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


def binary_search():
    pass
        
def main():
    a_list = [1,2,3,4,5,6,7]
    b = linear_search(a_list, 2)
    c = linear_search(a_list, 16)
    print(b, c, sep='\t')

    imdb_list = [{'title': 'Professional Help', 'actress': 'Big Chungus', 'score': 2}, {'title': 'Raising an error', 'actress': 'Big Cobra', 'score': 5}, {'title': 'Raise your voice', 'actress': 'Hilary Duff', 'score': 10}]
    chungus = linear_search(imdb_list, 'Big Chungus', func=lambda e: e['actress'])
    print(chungus)



    
if __name__ == '__main__':
    main()

