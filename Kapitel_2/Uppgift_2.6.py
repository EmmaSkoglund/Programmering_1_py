print("----------------------------")
print(":.      KOTVKOLLEN .:     ")
print("----------------------------")
print("Hur många elever vill ha...")

_2_korv = int(input("2 vanliga korvar        >"))
_3_korv = int(input("3 vanliga korvar        >"))
_2_vego = int(input("2 vegitariska korvar    >"))
_3_vego = int(input("3 vegitariska korvar    >"))

print("-----------------------------")
print(":.      INKÖPSLISTA        .:'")
print("-----------------------------")

antal_vanligakorvar = int(((_2_korv * 2 ) + (_3_korv * 3) + 7) /8)
antal_vegitariska = int(((_2_vego * 2 ) + (_3_vego * 3) + 3) /4)
antal_dryck = _2_korv + _3_korv + _2_vego + _3_vego
pris = float(antal_vanligakorvar * 20.95 + antal_vegitariska * 34.95 + antal_dryck * 13.95 )

print(antal_vanligakorvar)
print(antal_vegitariska)
print(antal_dryck)
print(pris,  " SEK ")