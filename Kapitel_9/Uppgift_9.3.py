firstNames =["Maria" , "Erik" , "Karl"]
lastNames =["Svensson" , "Karlsson" , "Andersson"]

fullNames = []

for firstName in firstNames:
    for lastName in lastNames:
        fullName = firstName + ' ' + lastName
        fullNames.append(fullName)

print(fullNames)

