import os
import random

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

cls()

vetX = []
copia = 0

for i in range (20):
    vetX.append(random.randint(0, 20))
print(vetX) 
print()

fim = 19
for i in range(10):
    copia = vetX[i]
    vetX[i] = vetX[fim]
    vetX[fim] = copia
    fim -= 1

print(f'O vetor após a troca ficou assim: {vetX}')    
