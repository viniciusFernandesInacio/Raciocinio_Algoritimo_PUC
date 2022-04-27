import sys


par = 0
impar = 0
for c in range(0,9):
    res = int(input(f'Digite o {c + 1}º número: '))
    if (res % 2 == 0):
        par += 1
    elif (res % 2 != 0):
        impar += 1
    else:
        print('[ERRO] Digite um valor valido!') 
        sys.exit(2) 
print('=' * 60)
print(f'Você digitou {par} números pares e {impar} números ímpares.')