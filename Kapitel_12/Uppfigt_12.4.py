notes = {
    'Meddelande fårn skolan': 'Friluftsdag på tisdag',
    'Kom ihåg!': 'Ta bilen till verkstad',
    'Inför tentamen': 'Gör alla instuderingsuppgifter'
}
for key in notes:
    print("Titel:\t", key)
    print("Text\t", notes[key])
    print("-" * 5)

while True:
    print("1. Lägg till artikel:")
    print("2. Ändra artikel:")
    print("3. Exit")

    choice = input("> ")

    if choice == "1":
        add_titel = input("titel > ")
        add_text = input("text > ")
        print("-" * 5)
        notes[add_titel] = add_text

    elif choice == "2":
        edit_title = input("titel > ")

        if edit_title in notes:
            new_titel = input("Ny titel > ")
            new_text = input("Ny text > ")
            notes[edit_title] = new_titel
            notes[new_titel] = new_text

        else:
            print("Titeln finns inte i listan \tvill du lägga till denna till listan? J/N")
            none_existed_titel = input("> ").lower()
            if none_existed_titel == "j":
                new_text = input("Ny text > ")
                notes[edit_title] = new_text
    elif choice == "3":
        break
    else:
        print("ogiltigt alternativ")

    for key in notes:
        print("Titel:\t", key)
        print("Text\t", notes[key])
        print("-" * 5)