import os
import random

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

cls()

#Criando a matriz.
matriz = []
num = int(input('Informe o número de linhas e colunas da matriz: '))
for i in range(num):
    matriz.append([])
    for j in range(num):
        matriz[i].append(random.randint(0,5))

#Imprime a matriz.
for i in range(len(matriz[i])):
    for j in range (len(matriz[i])):
        print(matriz[i][j], end = ' ' )
    print('') 
print('')    

#Realiza as somas.
soma_dp = 0
soma_ds = 0
soma_da = 0
soma_db = 0
soma_par = 0

for i in range(len(matriz)):
    for j in range(len(matriz)):
        if i == j:
            soma_dp += matriz[i][j]
        if (i + j == (len(matriz) - 1)):
            soma_ds += matriz[i][j]
        if i < j:
            soma_da += matriz[i][j]
        if i > j:
            soma_db += matriz[i][j] 
        if j % 2 == 0:
            soma_par += matriz[i][j]      
print(f'Diagonal principal = {soma_dp}.\nDiagonal secundária = {soma_ds}.\nAcima da diagonal = {soma_da}.\nAbaixo da diagonal principal = {soma_db}.\bColunas pares = {soma_par}')                     