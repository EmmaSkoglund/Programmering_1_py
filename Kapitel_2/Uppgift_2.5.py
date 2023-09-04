numbers = [] 

for i in range(5):
    num = int(input("Mata in heltal #" + str(i + 1) + ": "))
    numbers.append(num)

highest = max(numbers)

print("Det högsta talet är:", highest)