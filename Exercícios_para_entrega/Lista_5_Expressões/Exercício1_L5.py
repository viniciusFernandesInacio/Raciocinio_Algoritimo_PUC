import random

def criarMatriz(dimensao):
    matriz = [[random.randint(0,9) for x in range(dimensao)] for y in range(dimensao)]
    return matriz

def printMatriz(matriz):
    print(matriz)
num = int(input('Digite um número: '))
if (num != 0):
    printMatriz(criarMatriz(num)) 
else:
    print('[ERRO] O número deve ser diferente de 0.')            
