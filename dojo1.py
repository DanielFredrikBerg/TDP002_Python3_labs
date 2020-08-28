num = [int(input("Tal 1:")),int(input("Tal 2:")),int(input("Tal 3:"))]
print(num)
biggest = num[0]
smalest = num[0]
for i in range(1, len(num)):
    if num[i] > num[i-1]:
        biggest = num[i]
    if num[i] < num[i-1]:
        smalest = num[i]
print(biggest, smalest)
