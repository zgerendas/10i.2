import random

def genLista(db,kezd=1,veg=100):
    listam = list()
    for _ in range(db):
        #print(random.randint(1,100))
        listam.append(random.randint(kezd,veg))
    return listam
'''
l = genLista(10,20,30)
print(l)
l = genLista(10,1,45)
print(l)

l = genLista(10,50)
print(l)
'''

l = genLista(20,1,20)

# Másolás
def masolas(lista):
    lista2 = list()
    for elem in lista:
        lista2.append(elem*2)
    return lista2
print(masolas([3,7,1,4]))
l2 = masolas(l)
print(l,l2,sep="\n")

# kiválogatás

def kivalogatas(lista):
    lista2 = list()
    for elem in lista:
        if elem % 2 == 0:
            lista2.append(elem)
    return lista2
print(kivalogatas(l))

def maximum(lista):
    max = lista[0]
    for elem in lista:
        if elem > max:
            max = elem
    return max
print(maximum(l))

print(maximum(["barack","lama","alma","á","álmos"]))
szavak = ["barack","lama","alma","á","álmos"]
szavak.sort()
print(szavak)