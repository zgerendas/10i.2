def hasonlit(szam1,szam2):
    if szam1 > szam2:
        print(szam1,"a nagyobb")
    elif szam1 < szam2:
        print(szam2,"a nagyobb")
    else:
        print("Egyenlők")

hasonlit(1,5)
hasonlit(10,5)
hasonlit(5,5)

def osszeg(lista):
    osz=0
    for elem in lista:
        osz += elem
    return osz

print(osszeg([1,2,3,4]))

l=[32,66,3,3]
print(osszeg(l))

#l=[32,66,3,3,'a']

l=[32,66,3,3,78.8]
print(osszeg(l))

#l=["a","lama"]
#print(osszeg(l))
