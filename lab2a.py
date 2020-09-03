def frame(text):
    print((4+len(text))*"*")
    print("* "+text+" *")
    print((4+len(text))*"*")

def triangle(height):
    for i in range(height):
        print((1+2*i)*"*")

def flag(width):
    for i in range(9*width):
        if i == int(9*width/2):
            print()
        else:
            print(10*width*"*"+" "+10*width*"*")
