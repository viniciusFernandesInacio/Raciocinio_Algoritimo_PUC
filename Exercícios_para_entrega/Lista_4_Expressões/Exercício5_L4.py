import os
import random

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

cls()

#Criando a primeira matriz.
matriz1 = []
lin = int(input('Informe o número de linhas da matriz 1: '))
colu = int(input('Informe o número de colunas da matriz 1: '))
for i in range(lin):
    matriz1.append([])
    for j in range(colu):
        matriz1[i].append(random.randint(0,5))

#Imprime a primeira matriz.
for i in range(len(matriz1[i])):
    for j in range (len(matriz1[i])):
        print(matriz1[i][j], end = ' ' )
    print('') 
print('')

#Criando a segunda matriz.
matriz2 = []
lin = int(input('Informe o número de linhas da matriz 2: '))
colu = int(input('Informe o número de colunas da matriz 2: '))
for i in range(lin):
    matriz2.append([])
    for j in range(colu):
        matriz2[i].append(random.randint(0,5))

#Imprime a segunda matriz.
for i in range(len(matriz2[i])):
    for j in range (len(matriz2[i])):
        print(matriz2[i][j], end = ' ' )
    print('')  

#Soma das duas matrizes.
if(len(matriz1) != len(matriz2) or len(matriz1[0]) != len(matriz2[0])):
    print('[ERRO] As matrizes devem ter o mesmo número de linhas e colunas.')
res = []
for i in range (len(matriz1)):
    res.append([])
    for j in range(len(matriz1[0])):
        res[i].append(matriz1[i][j] + matriz2[i][j])
else:
    print('\nA soma das duas matrizes é igual a:\n')


for i in range(len(res[i])):
    for j in range (len(res[i])):
        print(res[i][j], end = ' ' )
    print('')      