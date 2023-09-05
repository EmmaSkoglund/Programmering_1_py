import random

ui_bredd = 20

print('.: THE HIGHER LOWER GAME :.')
print('-' * ui_bredd)
print('Welcome to The Higher Lower Game.')
print('I will randomise a number between 0 and 99.')
print('Can you guess it ?')
print('-' * ui_bredd)

secret_number = random.randint(0, 99)
guess= 0
attempts = 0
guess = int(input('Your guess > '))

while True:

    attempts += 1

    if guess < secret_number:
        guess = int(input("HIGHER! \nTry again > "))

    elif guess > secret_number:
        guess = int(input("LOWER! \nTry again > "))

    else:
        print(f'{secret_number} is correct!')
        print(f'It took you {attempts} guesses.')
        break