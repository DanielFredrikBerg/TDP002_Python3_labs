day = int(input("Mata in veckodagen: "))
month = int(input("Mata in antalet dagar i månaden: "))
print("må ti on to fr lö sö")
nums = list()
for i in range(day-1):
    nums.append(" ")
for i in range(month+1):
    nums.append(i+1)
for i in range(1, len(nums)):
    print('{0:2}'.format(nums[i-1]), end=" ")
    if not i%7:
        print()
