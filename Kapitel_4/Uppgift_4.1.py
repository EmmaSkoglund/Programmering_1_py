numbers = [] 

while True:
    tal = float(input("Ange ett tal: "))
    if tal < 0:
        break
    numbers.append(tal)

highest = max(numbers)
lower = min(numbers)
summa = sum(numbers) + len(numbers)
medel = sum(numbers) / len(numbers)

print('')
print(f"Lägsta tal: \t {lower} \nStörsta tal: \t {highest} \nSumma: \t \t {summa} \nMedelvärde: \t {medel} ") 