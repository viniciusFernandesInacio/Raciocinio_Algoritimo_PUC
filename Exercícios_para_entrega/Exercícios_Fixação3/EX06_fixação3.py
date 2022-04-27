soma = 0
cont = 0
print('=' * 40)
while True:
    res = float(input(f'Informe o {cont + 1} número (Digite 0 para parar a contagem).\n--> '))
    if res == 0:
        break
    soma = soma + res
    cont += 1
print('=' * 40)
print(f'A média de todos os valoeres é {soma / cont:.2f}')