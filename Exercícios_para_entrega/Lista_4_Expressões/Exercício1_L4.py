import os
import random

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

cls()

vetX = []
vetY = []
vetZ = []

for i in range (15):
    vetX.append(random.randint(0, 9))
print(vetX) 
print()

for i in range (20):
    vetY.append(random.randint(0, 9))
print(vetY)  
print()

for x in vetX:
    for y in vetY:
        achou = False # flag (Indica de o X já está em vetZ.)
        if (x == y):
            for z in vetZ:
                if (z == x):
                    achou = True
                    break
            if not(achou):
                vetZ.append(x)
                    
print(vetZ)
print()  