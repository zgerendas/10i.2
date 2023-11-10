import random
'''
for i in range(10):
    print(random.random())

for i in range(100):
    print(random.randint(1,100),end=", ")
'''
# random.seed(0)

gondolt = random.randint(1,100)
talalt = False
tippSzam = 0

while not talalt:   
    egesz = 0 
    while egesz < 1 or egesz > 100 :   
        egesz = int(input("Kérek egy 1 és 100 közé eső számit: "))
    tippSzam += 1
    if gondolt < egesz:
        print("Nagy")
    elif gondolt > egesz:
        print("Kicsi")
    else:
        print(tippSzam," Lépésben talált")
        talalt = True

print('-'*20)





