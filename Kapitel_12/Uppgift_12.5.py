notes = {
    'Meddelande fårn skolan': 'Friluftsdag på tisdag',
    'Kom ihåg!': 'Ta bilen till verkstad',
    'Inför tentamen': 'Gör alla instuderingsuppgifter'
}

remove_titel = input("Ta bort artikel: ")
print("-" * 5)
if remove_titel in notes:
    del notes[remove_titel]

for key in notes:
    print("Titel:\t", key)
    print("Text:\t", notes[key])
    print("-" * 5)