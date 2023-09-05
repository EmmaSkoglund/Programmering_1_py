tal: int = int(input('Ange multiplikationstabell >: '))
resultat = 0 

while True:
    for i in range(3):
        resultat += tal
        print(resultat)

    fortsätt = input("Vill du fortsätta: ")
    if fortsätt != "ja":
        break
    else:
        tre = 1
