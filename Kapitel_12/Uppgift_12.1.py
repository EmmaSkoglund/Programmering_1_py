notes = {
    'meddelande fårn skolan': 'Friluftsdag på tisdag',
    'kom ihåg': 'Ta bilen till verkstad',
    'inför tentamen': 'Gör alla instuderingsuppgifter'
}

anteckning = input("Anteckning > ").lower()

if anteckning in notes:
    print("-" * 10)
    print(notes[anteckning])
    print("-" * 10)
else:
    print("-" * 10)
    print("FEL: Anteckningar finns inte")
