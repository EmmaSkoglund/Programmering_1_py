# Definierar ny funktion, beräknar avståndet i kilometer till miles
# Resultatet retuneras från funktionen
def km_to_miles(km):
    miles = km * 0.621371
    return miles


# Definierar ny funktion, beräknar avståndet i miles till kilometer
# Retunerar resultatet från funktionen
def miles_to_km(miles):
    km = miles / 0.621371
    return km


# Hämtar input från användaren
distans = input("Ange distans > ")

#
dist = None

# Skapar en felhandetring för att frösöka dela strängen från
# användaren, choice får värdet och enhet får i detta fell km eller miles,
# omvandlar värdet till float
try:
    choice, enhet = distans.split(dist) # Deler upp strängen i två delar
    choice = float(choice.strip())
except ValueError:
    print("Fel angivelse") # Anger användaren fel visas detta

# Om km finns i strängen körs uträkningen från funktionen km_to_miles
if enhet == "km":
    resultat = km_to_miles(choice)
    print(f"{distans} motsvarar {resultat} miles")

# om miles finns i strängen, körs uräkningen från funktionen miles_to_km
elif enhet == "miles":
    resultat = miles_to_km(choice)
    print(f"{distans} motsvarar {resultat} kilometer")
