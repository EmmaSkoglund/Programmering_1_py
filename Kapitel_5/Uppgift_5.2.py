ui_bredd = 20

print(ui_bredd * '*')
print("* The Great Driver *")
print('-' * ui_bredd)
print('')
print('\t Beräknar c för uttrycket:'.center(ui_bredd))
print('\t a / b = c ')
print('')
print('-' * ui_bredd)

try:
    a = input('a = ')
    while True:
        A = float(a)
        break
except ValueError:
    print('FEL: Ogiltigt nummer ')

try:
    b = input('b = ')
    while True:
        B = float(b)
        break
except ValueError:
    print('FEL: Ogiltigt nummer ')

if A != 0 and B != 0:
    kvot = A / B
    print('-' * ui_bredd)

print(f' {A} / {B} = {kvot}')



