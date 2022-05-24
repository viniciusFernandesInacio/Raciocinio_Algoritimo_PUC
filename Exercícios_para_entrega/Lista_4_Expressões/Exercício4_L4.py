import os
import random

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

cls()

esc = int(input('Digite um número inteiro para ser usado como escalar: '))
lin = int(input('Digite o total de linhas da matriz: '))
colu = int(input('Digite o total de colunas da matriz: '))
matriz = []
lista = []
matriz_esc = []
for i in range(lin):
    linha = []
    for j in range(colu):
        num = random.randint(0,10)
        linha.append(num)
        matriz.append(linha) 
print(matriz)  
for i in range(lin):
    linha = []
    for j in range(colu):  
        linha.append(matriz[i][j] * esc)
        matriz_esc.append(linha)    
print(matriz_esc)          
    