import random

lista =[2,3,66,23,7,12,77]

# összegzés
osszeg = 0
for szam in lista: 
    #osszeg = osszeg + szam
    osszeg += szam
print(osszeg)

def osszgezes(listam):
    ossz = 0
    for szam in listam:
        ossz += szam
    return ossz
    
print(osszgezes([1,2]))
print(osszgezes(lista))

print(sum(lista))

# megszámolás
def megszamol(listam):
    db = 0
    for elem in listam:
        if elem > 50:
            db +=1
    return db
print(megszamol(lista))

lista2 = list()
for i in range(50):
    lista2.append(random.randint(1,100))
print(lista2)
print(megszamol(lista2))
db1 = megszamol(lista)
db2 = megszamol(lista2)
print(f"A két listában {db1+db2} darab 50-nél nagyobb szám volt." )
print("A két listában", db1+db2,"darab 50-nél nagyobb szám volt." )

# eldöntés
def vane(l):
    van = False
    for elem in l:
        #print(elem,end=",")
        if elem > 50:
            van = True
            break
    #print()
    return van

print(vane(lista))
print(vane([1,2,3,4,5]))
print(vane(lista2))
print("-"*10)
def vane2(l):
    van = False
    i = 0
    while not van and i < len(l):
        #print(l[i])
        if l[i] > 50:
            van = True
        i +=1
    return van

print(vane2(lista2))
print(vane2([1,2,3,4,5,49]))
print("+"*10)
# kiválasztás
def kivalasztHibas(l):
    van = False
    elem = None
    i = 0
    while not van and i < len(l):
        #print(l[i])
        if l[i] > 50:
            van = True
            elem = l[i]
        i +=1
    return elem
print(kivalasztHibas(lista),"-----")

def kivalaszt(l):
    van = False
    
    i = 0
    while not van and i < len(l):
        #print(l[i])
        if l[i] > 50:
            van = True
            
        i +=1
    return i
print(lista, kivalaszt(lista),"++++++")

def kivalaszt2(l):
    i =0 
    while not l[i] > 70:
        i +=1
    return i
print("Kivalaszt2:", kivalaszt2(lista))

# minimum
def minimum(l):
    mini = l[0]
    for elem in l:
        if elem < mini:
            mini = elem
    return mini
print(minimum(lista))
print(minimum(lista2))
print(minimum([-4,-56,4,5]))
print(minimum(["körte","alma","szilva"]))
