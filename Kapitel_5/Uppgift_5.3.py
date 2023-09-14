bredd = 15

numbers = []

print('.: MATHLETE :.')
print('-' * bredd)

while True:

    userInput = input('> ')

    if userInput == "exit":
        break

    try:
        number = int(userInput)
        numbers.append(number)

    except ValueError:
        print("FEL: Ogiltigt nummer ")

total, length = 0, 0

for number in numbers:
    total += number
    length += 1

average = total / length

print('-' * bredd)
print(f'Kardinalitet :{length} \nSumma :{total} \nMedelvärde :{average}')

