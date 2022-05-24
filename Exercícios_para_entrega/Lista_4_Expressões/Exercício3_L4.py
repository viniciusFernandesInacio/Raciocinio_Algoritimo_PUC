import random
import os

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

while True:
    cls()
    vet = []
    for c in range(30):
        vet.append(random.randint(0,9)) 
    print(vet)

    cont0 = 0
    for c in range (30):
        if vet[c] == 0:
            cont0 += 1 
    if cont0 > 0:
            print('O número 0 apareceu','1 vez.' if cont0 == 1 else f'{cont0} vezes.')    

    cont1 = 0
    for c in range (30):
        if vet[c] == 1:
            cont1 += 1 
    if cont1 > 0:
            print('O número 1 apareceu','1 vez.' if cont1 == 1 else f'{cont1} vezes.')               

    cont2 = 0
    for c in range (30):
        if vet[c] == 2:
            cont2 += 1 
    if cont2 > 0:
            print('O número 2 apareceu','1 vez.' if cont0 == 1 else f'{cont2} vezes.')               

    cont3 = 0
    for c in range (30):
        if vet[c] == 3:
            cont3 += 1 
    if cont3 > 0:
            print('O número 3 apareceu','1 vez.' if cont3 == 1 else f'{cont3} vezes.')               

    cont4 = 0
    for c in range (30):
        if vet[c] == 4:
            cont4 += 1 
    if cont4 > 0:
            print('O número 4 apareceu','1 vez.' if cont4 == 1 else f'{cont4} vezes.')               

    cont5 = 0
    for c in range (30):
        if vet[c] == 5:
            cont5 += 1 
    if cont5 > 0:
            print('O número 5 apareceu','1 vez.' if cont5 == 1 else f'{cont5} vezes.')               

    cont6 = 0
    for c in range (30):
        if vet[c] == 6:
            cont6 += 1 
    if cont6 > 0:
            print('O número 6 apareceu','1 vez.' if cont6 == 1 else f'{cont6} vezes.')               

    cont7 = 0
    for c in range (30):
        if vet[c] == 7:
            cont7 += 1 
    if cont7 > 0:
            print('O número 7 apareceu','1 vez.' if cont7 == 1 else f'{cont7} vezes.')               

    cont8 = 0
    for c in range (30):
        if vet[c] == 8:
            cont8 += 1 
    if cont8 > 0:
            print('O número 8 apareceu','1 vez.' if cont8 == 1 else f'{cont8} vezes.')               

    cont9 = 0
    for c in range (30):
        if vet[c] == 9:
            cont9 += 1 
    if cont9 > 0:
            print('O número 9 apareceu','1 vez.' if cont9 == 1 else f'{cont9} vezes.')               
    rep = str(input())
                 