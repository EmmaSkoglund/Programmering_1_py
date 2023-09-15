import json
import os

numbers = []
total = 0

with open('numbers.json', 'a+') as file:
    try:
        numbers = json.loads(file.read())
    except:
        numbers = []

while True:

    if os.name == 'nt':
            os.system('cls')
    else:
            os.system('clear')

    print(".: intMEMORIZER :. ")
    print("-" * 20)
    for interger in numbers:
        print("*", interger)
    print("-" * 20)
    if len(numbers) > 0:
        print("Sum - ", total)
    print("-" * 20)
    print("mata in heltal\n0 stänger scriptet")
    print("-" * 20)

    interger = int(input("> "))

    try:
        if interger == 0:
            break
        if interger in numbers:
            print()
        else:
            numbers.append(interger)
            total += interger

    except ValueError:
        print("FEL: Ogiltigt heltal ")

with open('numbers.json', 'w') as f:
    f.write(json.dumps(numbers))













