#bild1
def main1():
    numbers = [1,2,3]
    numbers_reference = numbers
#bild2

def main2():
    numbers = [1,2,3]
    numbers_reference = numbers.copy()

#bild 3
def add_element(l, e):
    l.append(e)
def main3():
    numbers = [1 ,2 ,3]
    add_element(numbers, 4)
main()

#bild 4
def add_element1(l, e):
    l.append(e)
def main4():
    numbers = [1 ,2 ,3]
    add_element1(numbers.copy(), 4)
main1()
main2()
main3()
main4()
