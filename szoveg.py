#mondat = input("Kérek egy mondatot! :")
mondat = 'Ez egy teszt mondat ide írtam, hogy nem!!'
print(len(mondat))

db = 0
for c in mondat:
    # print(c)
    if c == 'e' or c == 'E':
        db +=1
print(db,"darab e betű volt")

db = 0
for c in mondat.lower()  :
    if c == 'e':
        db +=1
print(db,"darab e betű volt")

maganhangzok = ('a','á','e','é','i','í','o','ó','ö','ő','u','ú','ü','ű')
"""
print(mondat)
print(mondat.find('e'))
print(mondat.find('g'))
print(mondat.find('E'))
print(mondat.find('hogy'))
print(mondat.find('x'))

print(mondat.index('e'))
print(mondat.index('g'))
print(mondat.index('E'))
print(mondat.index('hogy'))
print(mondat.index('x'))
"""
'''
db = 0

magan=set()
print(type(magan))
for c in mondat.lower()  :
    for m in maganhangzok:
        if c == m:
            db +=1
            magan.add(c)

print(db,"Magánhangzó volt")
print(len(magan),"darab különböző magánhangzóm volt")

mondat="Vettem egy kiló almát, almaszószt készítek belőle."

print(mondat)
print(mondat.replace("alma","körte"))
print(mondat)
mondat2 = mondat.replace("e","a")
print(mondat2)

mondat2 = mondat.replace("e","a",2)
print(mondat2)

#mondat2 = mondat.replace("e","a",2,3)
#print(mondat2)
print(mondat.split(" "))
print(mondat.split(","))
print(mondat.split("al"))

print(mondat.count("al"))

mondat="á"
print(mondat.encode("latin2"))
print('-'*10)
print(mondat.encode("utf-8"))
print('*'*10)
print(mondat.encode("utf-16"))
print('*'*10)
print(mondat.encode("utf-32"))
'''
#mondat.format("","")
print(mondat.isdecimal())
print("12".isnumeric())

#szam = int(input("Kérek egy egész szamot!: "))
'''
ismeteld = True
while ismeteld:
    szam = input("Kérek egy egész szamot!: ")
    if szam.isdecimal():
        egesz=int(szam)
        ismeteld = False
print(egesz)
'''

print("Alma12ekes".isalnum())
print("Alma12ékes".isalnum())
print("Alma12,ékes".isalnum())
print(mondat)
print('----------')
print(mondat.join("egy"))
print('----------')
print(mondat)

lista = ["alma","barack","szilva"]
print(" vettem ".join(lista))
print(",".join(lista))
x = ",".join(lista)
print(x.split(","))

mondat.