heltal = input('Ange ett heltal: ')

try:
    tal =int(heltal)
    print("resultat:", (tal*2))
except ValueError:
    print("Fel:" "'" + heltal + "'" "kan inte översättas till ett heltal")