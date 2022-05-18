import os
import random

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

cls()

#Preenche a matriz m1 com números aleatórios e printa ela
m1 = []
for i in range(3):
    lin = []
    for j in range(3):
        lin.append(random.randint(1,7))
    m1.append(lin)    
for i in range(3):
    for j in range(3):
        print(m1[i][j], end=' ')

#Preenche a matriz m2 com números aletórios e printa ela
m2 = []
for i in range(3):
    lin = []
    for j in range(3):
        lin.append(random.randint(1,7))
    m2.append(lin)    
for i in range(3):
    for j in range(3):
        print(m2[i][j], end=' ')

#Soma as matrizes m1 e m2 em uma unica matriz m3
m3 = []
for i in range(3):
    lin = []
    for j in range(3):
        lin.append(m1[i][j] + m2[i][j])               

