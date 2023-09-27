# Skapa en klass Person med attribut för namn, ålder och adress.
# Skapa en metod som returnerar en kort beskrivning av personen.

class Person:
  def __init__(self, name, age, adress):
    self.name = name
    self.age = age
    self.adress = adress

p = Person("Emma", 23, "kvistväken 7")
print(p.name)
print(p.age)
print(p.adress)