mondat = "Aliqua cupidatat incididunt et commodo quis culpa elit labore id sint aute."

lista = mondat.split(" ")
print(len(lista))

mondat = "Aliqua     cupidatat            incididunt et commodo quis culpa elit labore id sint aute."

lista = mondat.split(" ")
print(len(lista))
print(lista)

mondat2 = mondat
print(mondat.replace("  "," "))
print(mondat)

while len(mondat) > len(mondat.replace("  "," ")):
    mondat = mondat.replace("  "," ")
print(mondat)

#print(mondat2.strip(" "))

lista = mondat2.split(" ")
print(lista)

"""
for szo in lista:
    if szo == '':
        #print(szo,"+")
        lista.remove('')  # !!!!!!! tilos a lista módosítása
        print(lista)
"""      
lista2 = []
print(type(lista2))


for szo in lista:
    if szo != '':
        #print(szo,"+")
        lista2.append(szo)
        #print(lista2)
print(len(lista2))

lista2 = lista
for i in range(len(lista)-1,-1,-1):
    if lista[i] == '':
        lista2.pop(i)
print(lista2)

magan = 'euioa'
for c in magan:
    print(c,mondat.count(c))