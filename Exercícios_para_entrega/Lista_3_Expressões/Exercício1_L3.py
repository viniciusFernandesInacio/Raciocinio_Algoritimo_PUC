'''Escreva um programa que leia um conjunto de números inteiros e que somente termine a leitura 
quando for digitado o valor 0 (zero) como finalizador. Informe então quantos números foram 
fornecidos e qual é a média do conjunto (desconsidere o finalizador).'''

soma = 0
cont = 0
print(40 * '=')
while True:
    res = int(input('Digite um número [Digite 0 para parar a contagem].\n-->'))
    if (res == 0):
        break
    soma += res
    cont += 1
print(40 * '=')
print(f'Você digitou um total de {cont} números e a média entre eles é {soma / cont:.}')    