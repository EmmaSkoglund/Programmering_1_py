todo = ['Städa', 'Handla', 'Plugga', 'Ge blod ']
ny = input('Ange todo: ')

if ny not in todo:
    print(f'{ny} finns inte i listan. ')
    val = input('Vill du lägga till denna (J/N)? ')
    if val.lower() == 'j':
        todo.append(ny)
        print('Todo tillagd! ')
    else:
        print('Ingen ändring i listan. ')
else:
    print(f'{ny} finns redan i listan ')



