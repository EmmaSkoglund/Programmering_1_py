registrerade = ['Anna', 'Eva ', 'Erik', 'Lars', 'Karl']
avanmälningar = ['Anna', 'Erik', 'Karl'
                 ]
for person in avanmälningar:
    if person in registrerade:
        registrerade.remove(person)
print("Uppdaterad registreringslista:", registrerade)
