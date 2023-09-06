import os
ui_bredd = 20

POST_1 = ''
POST_2 = ''
POST_3 = ''

while True:

    if os.name == 'nt':
        os.system('cls')
    elif os.name == 'posix':
        os.system('clear')

    print('.: basicBILLBOARD :.')
    print('*' * ui_bredd)
    print('P1:', POST_1)
    print('P2:', POST_2)
    print('P3:', POST_3)
    print('-' * ui_bredd)
    print('c  Ändra post')
    print('e  Stäng program')

    meny = input('meny > ')

    if meny == 'c':
        id = input('id > ')
        if id == '1':
            meddelande = input('meddelande > ')
            POST_1 = meddelande

        elif id == '2':
            meddelande = input('meddelande > ')
            POST_2 = meddelande

        elif id == '3':
            meddelande = input('meddelande > ')
            POST_3 = meddelande

    elif meny == 'e':
        break

    if meny != 'c':
        print(f'- FEL: okänt kommando ({meny})')
        print('-' * ui_bredd)
        print('Tryck enter för att fortsätta...')

    if id != ['1', '2', '3']:
        print(f'- FEL: Felaktigt ID ')
        print('- INFO: Vänligen ge heltel mellan 1-3')
        print('-' * ui_bredd)
        print('Tryck enter för att fortsätta...')


