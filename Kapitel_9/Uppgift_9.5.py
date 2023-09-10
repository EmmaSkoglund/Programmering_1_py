import os
from typing import List

bredd = 30

lists = []

while True:

    if os.name == 'nt':
            os.system('cls')
    else:
            os.system('clear')

    print('.: Stackmaster :. '.center(bredd))
    print('-' * bredd)
    if len(lists) == 0:
        print("Empty\n:(".center(bredd))
    else:
        for line in lists:
          print('-', line)
    print('-' * bredd)
    print('| Meny |'.center(bredd))
    print('-' * bredd)
    print('push | Push element to stack')
    print('pull | Pull element from stack ')
    print('exit | Exit program')
    print('-' * bredd)

    choose = input('Meny > ')

    if choose == 'pull':
        try:
            lists.pop()
            print('-' * bredd)
        except IndexError:
            print('Error stack is empyt ')
            input("Press enter to continue...")

    elif choose == 'push':
        print('-' * bredd)
        add_item = input('ITEM > ')
        lists.append(add_item)
        print('-' * bredd)

    elif choose == 'exit':
        break

    else:
        print('ERROR: Unknown command \nPress enter to continue... ' )
        input()


