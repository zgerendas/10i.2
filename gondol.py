import random
'''
for i in range(10):
    print(random.random())

for i in range(100):
    print(random.randint(1,100),end=", ")
'''

gondolt = random.randint(1,100)

egesz = 0 
while egesz < 1 or egesz > 100 :   
    egesz = int(input("Kérek egy 1 és 100 közé eső számit: "))

print(egesz)





