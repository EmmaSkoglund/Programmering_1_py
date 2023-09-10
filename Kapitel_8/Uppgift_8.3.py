todo = ['Städa', 'Handla', 'Plugga', 'Ge blod', 'Hämta barn ']
print(todo)
index = int(input('Ta bort todo (index): '))
if 0 <= index < len(todo):
    bort = todo.pop(index)
print(todo)
