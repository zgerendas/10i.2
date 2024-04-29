def kicsi(lista):
    k = lista[0]
    for e in lista:
        if e < k:
            k = e
    return k

print(kicsi([3,5,7,1]))

def nagy(lista):
    n = lista[0]
    for e in lista:
        if e > n:
            n = e
    return n
print(nagy([3,5,7,1]))


szamok = list()
ismet = True
while ismet:
    sz = input("Kérek egy számot: ")
    if sz == "":
        ismet = False
    else:
        szamok.append(int(sz))
print(szamok)


def harommalOsztahtok(lista):
    db = 0


    return db
    


