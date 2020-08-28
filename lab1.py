print("Uppgift 1a")
a = 0
for i in range(129):
    a += i
    
print(a, "\n\nUppgift 1b")
a = 1
for i in range(1, 13):
    a = a * i
    
print(a, "\n\nUppgift 1c")
a = 0
notDivisible = True
while notDivisible:
    a+=1
    for i in range(1, 11):
        if a%i:
            break
        elif i == 10:
            notDivisible = False

print(a, "\n\nUppgift 1d")
primes = [2]
for i in range(2, 1000):
    for j in range(2, i):
        if i%j==0:
            break
        elif j == i-1:
            primes.append(i)
a = 0
for i in range(len(primes)):
    a += primes[i]
print(a)
