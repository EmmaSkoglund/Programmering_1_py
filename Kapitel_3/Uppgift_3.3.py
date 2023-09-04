import random

dice = random.randint(1, 6)

if dice == 1:
    print("Du slog en 1:a!")
    print("---------")
    print("|       |")
    print("|   X   |")
    print("|       |")
    print("---------")  
elif dice == 2: 
    print("Du slog en 2:a!")
    print("---------")
    print("| X     |")
    print("|       |")
    print("|     X |")
    print("---------")
elif dice == 3:
    print("Du slog en 3:a!")
    print("---------")
    print("| X     |")
    print("|   X   |")
    print("|     X |")
    print("---------")
elif dice == 4:
    print("Du slog en 4:a!")
    print("---------")
    print("| X   X |")
    print("|       |")
    print("| X   X |")
    print("---------")
elif dice == 5:
    print("Du slog en 5:a!")
    print("---------")
    print("| X   X |")
    print("|   X   |")
    print("| X   X |")
    print("---------")
else:
    print("Du slog en 6:a!")
    print("---------")
    print("| X   X |")
    print("| X   X |")
    print("| X   X |")
    print("---------")
    