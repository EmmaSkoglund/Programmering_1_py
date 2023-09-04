tal1 = int(input("Ange tal 1: "))
störsttal = tal1
tal2 = int(input("Ange tal 2: "))

if tal2 > tal1:
    störsttal = tal2
tal3 = int(input("Ange tal 3: "))

if tal3 > tal1 or tal3 > tal2:
    störsttal = tal3

print(f"Största talet är: {störsttal}")