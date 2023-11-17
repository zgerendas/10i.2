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

