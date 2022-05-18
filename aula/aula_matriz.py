import os
import random

def cls():
    os.system('cls' if os.name == 'nt'else 'clear')

cls()

#m = [[1,2,3], [4,5,6], [7,8,9]]

m = []
#Preenche a matriz com números aleatórios
for i in range(3):
    lin = []
    for j in range(3):
        lin.append(random.randint(1,5))
    m.append(lin)

#Printa a matriz
for i in range(3):
    for j in range(3):
        print(m[i][j], end=' ')
    print()            

soma = 0
for i in range(3):
    soma_linha = 0
    for j in range(3):
        soma += m[i][j]
        soma_linha += m[i][j]
    print(m[i], end=' ')  
    print(f'Soma linha = {soma_linha}.')    
print('A soma dos elementos é igual a', soma)        