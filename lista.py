
'''
lista = [1,2,3,4,5]
lista2 = lista

lista2.append(6)
print(lista2)
print(lista)

a = 12
b = a
b +=1
print(a,b)

lista3 = lista.copy()
lista3.append(7)
print(lista,lista2,lista3,sep="\n")

halmaz1 ={1,2,3,4,4}
print(halmaz1)
halmaz2 = halmaz1
halmaz2.add(5)
print(halmaz1,halmaz2,sep="\n")
halmaz3 = halmaz1.copy()
halmaz3.add(6)
print(halmaz1,halmaz2,halmaz3,sep="\n")

halmaz1.clear()
print(halmaz1,halmaz2,halmaz3,sep="\n")
print('-'*10)
lista.clear()
print(lista,lista2,lista3,sep="\n")

lista = [1,2,3]
print(lista,lista2,lista3,sep="\n")

lista.append(lista3)
print(lista)
lista3.append('Alam')
print(lista,lista3,sep="\n")
print('-'*10)


lista = [1,2,3]
lista3 = [4,5,6]
lista.append(lista3.copy())

lista3.append("Alma")
print(lista,lista3,sep="\n")

'''
'''
lista =[]
szam = 1
while szam != 0:
    be = input("Kérek egész számot, 0 - vége: ")
    if be.isnumeric():
     #isdecimal():
        szam = int(be)
        lista.append(szam)
print(lista)

lista = [5,12,9,77,-11]
lista2 = lista.copy()
lista.sort()
print(lista)

lista.sort(reverse=True)
print(lista,lista2)

lista2.reverse()
print(lista2)

print(lista2.count(77))
lista2.append(77)
print(lista2.count(77))
print(lista2.count(777))

lista2.extend(range(10))
print(lista2)

lista2.extend(lista)
print(lista2)

print(lista2.index(12))
#print(lista2.index(-12))

lista2.insert(3,"Alma")
print(lista2)

lista2.remove(2)
print(lista2)

#lista2.remove("alma")
lista2.remove("Alma")
print(lista2)

lista2.remove()
'''

import random
szamok = list()
for i in range(100):
    v = random.randint(1,100)
    if szamok.count(v) == 0 :
        szamok.append(v)
szamok.sort()
print(szamok)


szamok = list()
while len(szamok) < 100:
    v = random.randint(1,100)
    if szamok.count(v) == 0 :
        szamok.append(v)
print(szamok)
szamok.sort()
print(szamok)


szamok = list()
while len(szamok) < 5:
    v = random.randint(1,90)
    if szamok.count(v) == 0 :
        szamok.append(v)
print(szamok)
szamok.sort()
print(szamok)
