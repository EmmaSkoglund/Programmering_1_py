def oversatt_till_rovarspraket(text):

    konsonanter = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    resultat = ''
    index = 0

    while index < len(text):
        tecken = text[index]
        if tecken in konsonanter:
            resultat += tecken + "o" + tecken
        else:
            resultat += tecken

        index += 1

    return resultat

text = input("Ange en text: ")

resultat = oversatt_till_rovarspraket(text)

print("Översatt till rövarspråket:", resultat)
