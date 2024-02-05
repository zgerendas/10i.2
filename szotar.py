'''
v = {}
print(type(v))

v = []
print(type(v))

v = ()
print(type(v))
print('*'*10)

v = set()
print(type(v))
v.add(1)
v.add(2)
v.add(1)
print(v)

v = list()
print(type(v))
v.append(1)
v.append(2)
v.append(1)
print(v)

v = tuple()
print(type(v))


v = dict()
print(type(v))


szotar ={"nev":"Pista", "kor":14}
print(szotar)
print(szotar["nev"])

sor = "Laborum Lorem laborum do tempor nisi cupidatat dolore do."
lista = sor.replace(".","").split(" ")
#print(lista)

szavak = dict()
kulcs = 1
for szo in lista:
    #print(szo)
    szavak.update({kulcs:szo})
    kulcs += 1
print(szavak)

for x in szavak:
    print(x,end=", ")
print()

szotar.update({"datum":1999})
szotar["város"]="Budapest"
print(szotar)
for x in szotar:
    print(x,end=", ")
print()


for kulcs in szotar:
    print(kulcs,szotar[kulcs])
print()


for x in szotar.keys():
    print(x,end=", ")
print()


for x in szotar.values():
    print(x,end=", ")
print()

for k,e in szotar.items():
    print("kulcs: ",k,"\térték: ",e)

'''
szemelyek = list()
szemely = {"név":"Pista","kor":14,"nem":"fiú"}
szemelyek.append(szemely)

szemely = {"név":"Ági","kor":13,"nem":"lány"}
szemelyek.append(szemely)

szemely = {"név":"Bori","kor":15,"nem":"fiú"}
szemelyek.append(szemely)

szemely = {"név":"Zalán","kor":14,"nem":"fiú"}
szemelyek.append(szemely)

print(szemelyek)

for szem in szemelyek:
    print(szem["név"])

for szem in szemelyek:
    if szem["nem"] == "fiú":
        print(szem["kor"])

osszeg = 0
#db = 0
for szem in szemelyek:
    osszeg += szem["kor"]
 #   db +=1

print(osszeg/len(szemelyek))
#print(db, len(szemelyek))

db = 0
osszeg = 0
for szem in szemelyek:
    if szem["nem"] == "fiú":
        osszeg += szem["kor"]
        db +=1
print(osszeg/db)


for szem in szemelyek:
    szem["kor"] +=1
print(szemelyek)



