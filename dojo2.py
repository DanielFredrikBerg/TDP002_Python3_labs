loan = int(input("Vad är lånet?"))
rate = int(input("Vad är räntan?"))
needsChecking = True
while needsChecking:
    if loan > 100:
        loan = int(input("lånet ska vara mindre än 100, skriv igen: "))
    elif rate > 100:
        rate = int(input("räntan ska vara mindre än 100, sriv igen: "))
    elif loan < 0:
        loan = int(input("lånet ska vara större än 0, skriv igen: "))
    elif rate < 0:
        rate = int(input("räntan ska vara större än 0, skriv igen: "))
    else:
        needsChecking = False
for i in range(12):
    print(i+1, ".", loan, rate)
    loan += loan * rate/100
