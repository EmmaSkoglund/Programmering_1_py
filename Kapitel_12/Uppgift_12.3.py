notes = {
    'Meddelande fårn skolan': 'Friluftsdag på tisdag',
    'Kom ihåg!': 'Ta bilen till verkstad',
    'Inför tentamen': 'Gör alla instuderingsuppgifter'
}

print("-" * 5)

for key in notes:
    print("Titel:\t", key)
    print("Text:\t", notes[key])
    print("-" * 5)