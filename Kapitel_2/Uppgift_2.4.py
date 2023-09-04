ålder = int(input ("Ange din ålder: "))
if ålder < 18:
    myndig = 18 - ålder
    print ("Det är" , myndig , "år kvar tills du blir myndig ")
else:
    print ("Du är myndig ")