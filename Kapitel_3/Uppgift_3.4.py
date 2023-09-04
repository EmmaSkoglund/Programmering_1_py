land = str(input("Ange ett land: "))
land = land.lower()

if land == "Danmark" or "Finland" or "Island" or "Norge" or "Sverige":
    print(land, "tillhör norden. ")
elif land == "England" or "Nordirland" or "Skottland" or "Wales":
    print(land, "tillhör Storbritanien ")
else:
    print(land, "tillhör varken norden eller Storbritanien ")