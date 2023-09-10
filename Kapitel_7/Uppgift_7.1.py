import os
ui_bredd = 20

POST_1 = ''
POST_2 = ''
POST_3 = ''

while True:

    # Rensar terminalfönster
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

    # Skriver ut instruktioner
    print('.: basicBILLBOARD :.')
    print('*' * ui_bredd)
    print('P1:', POST_1)
    print('P2:', POST_2)
    print('P3:', POST_3)
    print('-' * ui_bredd)
    print('c  Ändra post')
    print('e  Stäng program')

    # Hämtar komando från användaren
    meny = input('meny > ')

    # Utför opperationer för inmatat kommando
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

        elif id != '1, 2, 3':
            print(f'- FEL: Felaktigt ID ')
            print('- INFO: Vänligen ge heltel mellan 1-3')
            print('-' * ui_bredd)
            input('Tryck enter för att fortsätta...')

    elif meny == 'e':
        break

    if meny != 'c':
        print(f'- FEL: okänt kommando ({meny})')
        print('-' * ui_bredd)
        input('Tryck enter för att fortsätta...')



