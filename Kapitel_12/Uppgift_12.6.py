import os
import json

bredd = 19

notes = {
    "Important" : "Lite test och annat",
    "Notes from lecture" : "testar..."
}

with open('notes.json','a+') as f:
    try:
        notes = json.loads(f.read())
    except:
        notes = {}


while True:

    if os.name == 'nt':
            os.system('cls')
    else:
            os.system('clear')

    print('.: ALWAYSNOTE :.')
    print('-- gold edition --')
    print('*' * bredd)
    for key in notes:
        print('-', key)
    print('-' * bredd)
    print('view | view note')
    print('add  | add note')
    print('rm   | remove note')
    print('exit | exit program')
    print('-' * bredd)

    option = input('meny > ')
    print('-' * bredd)

    if option == 'view':
        title = input('title > ')
        print(notes[title])

    elif option == 'add':
        title = input('title > ')
        descr = input('descr > ')
        notes[title] = descr
        print('-' * bredd)
        print('INFO: Note added')

    elif option == 'rm':
        title = input('title > ')
        del notes[title]
        print('-' * bredd)
        print('INFO: Note delited')

    elif option == 'exit':
        print('Saving to notes.json...')
        with open('notes.json', 'w') as f:
            f.write(json.dumps(notes))
        print('Programmet stängdes')
        break

    else:
        print(f'ERROR: Unknown command ({option})')
        print('-' * bredd)
        input('Press enter to continue...')



