text = input('Ange en text: ')
bokstav = input('Ange en bokstav: ')

antal_forekomster = 0
index = 0

while index < len(text):
    aktuell_bokstav = text[index].lower()

    if aktuell_bokstav == bokstav:
        antal_forekomster += 1

    index += 1

print(f"Bokstaven '{bokstav}' förekommer {antal_forekomster} gånger i texten.")
