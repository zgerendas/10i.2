import random

# 1. Feladat
ismeteld = True
szamok = list()
while ismeteld:
    szamStr = input("Kérek egy számot: ")
    if szamStr != "":
        szam = float(szamStr)
        szamok.append(szam)
        #szamok.append(float(szamStr))
    else:
        ismeteld = False
    #print(szam)
print(max(szamok))
print(min(szamok))
# min
minimum = szamok[0]
for elem in szamok:
    if elem < minimum:
        minimum = elem
print(f"A listában {minimum} a legkisebb.")

maximum = szamok[0]
for elem in szamok:
    if elem > maximum:
        maximum = elem
print(f"A listában {maximum} a legnagyobb.")

# 2.a
#l = [2,3,4,5,6,7,8,9]

def harommal_oszthatok(lista):
    db = 0
    for szam in lista:
        if szam % 3 == 0:
            db +=1
    return db
#print(harommal_oszthatok(l))
# 2.b

szamok = list() #
for _ in range(20):
    #print(_,random.randint(1,100))
    szamok.append(random.randint(1,100))
# 2.c
print(f"A listában {harommal_oszthatok(szamok)} darab hárommal osztható szám szerepelt.")

