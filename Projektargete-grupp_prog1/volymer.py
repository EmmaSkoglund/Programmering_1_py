import os
from class_volume import Volume

class_volume = Volume
volume_calculator = Volume()


def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


while True:
    clear_screen()
    print("-" * 30)
    print("Här kan du räkna ut volymer!")
    print(" ")
    print("Du kan välja mellan att räkna\nut volymen på")
    print("-" * 5)
    print("1: Kub\n2: Rätblock\n3: Prisma\n4: Cylinder\n5: Eget val")
    print("-" * 5)

    val = input("Välj ett av alternativen åvan genom att ange dess fiffra!\n> ")

    if val == "1":
        print("-" * 30)
        print("Här kan du se formeln för hur\nman räknar ut volymen aven kub")
        print("-" * 5)
        print("Volym = a ⋅ a ⋅ a = a**3")
        print("-" * 5)
        print("Annars kan du mata in sidornas längd för att få det uträknat")
        try:
            sida = float(input("Ange längd på sida  > "))
            volym = volume_calculator.kub_volym(sida)
            print(f"Volymen på kuben är {volym}")
        except ValueError:
            print("Felaktig inmatning. Ange en giltig längd.")

        fortsätt = input("Vill du forsätta till nästa? J/N > ").lower()
        if fortsätt == "n":
            break

