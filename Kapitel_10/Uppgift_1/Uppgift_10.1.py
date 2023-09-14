import os

with open('sign.txt', 'r') as f:
    note = f.read()

while True:

    if os.name == 'nt':
            os.system('cls')
    else:
            os.system('clear')

    print('|-----------------------------------------|')
    print('|  #  ------------------------       #    |')
    print('| ### |   ', note, '         |  #  ###    |')
    print('| ###  ----------------------- ### ###    |')
    print('|  |        |         |         |   |   # |')
    print('|-----------------------------------------|')
    print('| C | Change sign message')
    print('| E | Exit program')
    print('|-------------------------')

    choice = input('> ')

    if choice.lower() == 'c':
        print('|-------------------------')
        message = input('Enter new message:\n> ')
        note = message
        with open('sign.txt', 'w') as f:
            f.write(note)


    elif choice.lower() == 'e':
        break

    else:
        print(f'| ERROR: Unknown command ({choice})\n| Press enter to continue...')

