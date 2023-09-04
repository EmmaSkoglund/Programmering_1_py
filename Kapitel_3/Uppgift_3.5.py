kön = input("Ange kön: ").lower()
hårfärg = input("Ange hårfärg: ").lower()
ögonfärg = input("Ange ögonfärg: ").lower()

if kön == "kvinna" and hårfärg == "brun" and ögonfärg == "brun":
    print("----------------")
    print("Egenskaperna matchar med : Emma Watson, Selina Gomez ")

elif kön == "kvinna" and hårfärg == "blond" and ögonfärg == "blå":
    print("----------------")
    print("Egenskaperna matchar med : Taylor Swift, Miley Cyrus ")

elif kön == "kvinna" and hårfärg == "brun" and ögonfärg == "blå":
    print("----------------")
    print("Egenskaperna matchar med : Angelina Jolie ")

elif kön == "man" and hårfärg == "röd" and ögonfärg == "blå":
    print("----------------")
    print("Egenskaperna matchar med : Rupert GrintS, Ed Sheeran")

elif kön == "man" and hårfärg == "brun" and ögonfärg == "brun":
    print("----------------")
    print("Egenskaperna matchar med : Daniel Radcliffe, Jonny Depp ")

else:
    print("Personen du söker finns inte i listan ")