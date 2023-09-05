ui_bredd = 20

print(ui_bredd * '*')
print("* The Great Driver *")
print('-' * ui_bredd)
print('')
print('\t Beräknar c för uttrycket:'.center(ui_bredd))
print('\t a / b = c ')
print('')
print('-' * ui_bredd)

while True:
    try:
        a = float(input('a = '))
        if a == 0:
            print('-' * ui_bredd)
            print("FEL : Division med 0")
        else:
            break
    except ValueError:
        print('FEL: Ogiltigt nummer ')

while True:
    try:
        b = float(input('b = '))
        if b == 0:
            print('-' * ui_bredd)
            print('FEL : Division med 0')
        else:
            break
    except ValueError:
        print('FEL: Ogiltigt nummer ')

try:
    if a != 0 and b != 0:
        kvot = a / b
        print('-' * ui_bredd)
        print(f' {a} / {b} = {kvot}')
except ValueError:
    print('FEL: Ogiltigt nummer ')

