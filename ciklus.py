# for (i = 0; i < 10 ; i++) { ..... } pl java  script
# while
'''
sor = [1,2,3,5,7]
for i in sor:
    print(i)
    print(i*i)
print('-'*10)

sor = {1,2,3,5,7,2,3}
for i in sor:
    print(i,end="; ")
    print(i*i)
print('-'*10)


sor = (1,2,3,5,7,2,3)
for i in sor:
    print(i,end="; ")
    print(i*i)
print('-'*10)

#sor = [1,2,3,5,"szöveg",["a","b"]]
# ! nem ok sor = {1,2,3,5,"szöveg",["a","b"]}
# ! nem ok sor = {1,2,3,5,"szöveg",{"a","b"}}
sor = {1,2,3,5,"szöveg",("a","b")}
sor = (1,2,3,5,"szöveg",["a","b"])

for i in sor:
    print(type(i),i)

for i in [1,2,3,4,5,6,7,8,9,10]:
 print(i,end=", ")
print()

for i in range(100): # for (i = 0; i < 100; i++) {}
    print(i,end=", ")
print()

for i in range(1,11): 
    print(i,end=", ")
print()

for i in range(1,21,3): 
    print(i,end=", ")
print()

for i in range(10,-11,-2): 
    print(i,end=", ")
print()

lista = ["alma","körte","barack",1,2,3]
db = 1
for i in lista:
    print(db,i,sep="; ")
    #db = db + 1
    db += 1         # +=x ; -=x; *=x; /=x %=x //=x

db = 13
db %= 2
print(db)

db = 13
db //= 2
print(db)

print(len(lista))
print(lista,lista[2],lista[1])

for i in range(len(lista)):
    print(i,lista[i])

print("*"*10)
lista = [1,2,3,["a","b"]]
for i in range(len(lista)):
    print(i,lista[i])
print("*"*10)

lista = [[1,2],[3,4],[5,6]]
for i in range(len(lista)):
    print(i,lista[i])

for i in lista:
    print(i)

for i,j in lista:
    print(i,j)

db = 1
for i,j in lista:
    print(db,i,j,sep=", ")
    db  += 1

#for i,j in [[1,2,10],[3,4],[5,6]]:
#    print(i,j)


ismet = True
while ismet :
    # print("Valami")
    egesz = int(input("Kérek egy 1 és 10 közé eső számit: "))
    if egesz >=1 and egesz <= 10:
        ismet = False
    else:
        print("Hibás a szám: ",egesz)

print(egesz)

i = 0
while i < 10:
    print(i)
    i += 1

print("ciklus vege ",i)

'''
i = 0
while i < 10:
    i += 1
    print(i,end=" - ")
    if i == 5:
        continue
    print(i*i) 
    if i == 7:
        break
print("ciklus vege ",i)





