def berakna_sovbehov(ålder):

    if ålder == 1:
        return "14 timmar"
    elif ålder == 2:
        return "13 timmar"
    elif ålder == 3:
        return "12 timmar"
    elif ålder == 4:
        return "11,5 timmar "
    elif ålder in [5,6]:
        return "11 timmar "
    elif ålder == 7:
        return "10,5 timmar "
    elif ålder in [8,9,10]:
        return "10 timmar "
    elif ålder == 11:
        return "9,5 timmar "
    elif ålder in [12,13,14,15]:
        return "9 timmar "
    elif ålder == 16:
        return " 8,5 immar "
    else:
        return "8 timmar "
    
namn = input("Ange ditt fullständiga namn: ")
ålder = int(input("Ange din ålder "))
print("_______________________")
    
meddelande = f"Hallå {namn}! Enligt Vårdguidens rekomendationer behöver indevider i din ålder ({ålder}) sova minst  "
print(meddelande)