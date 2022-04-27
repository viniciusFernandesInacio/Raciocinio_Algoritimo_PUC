numero = 2
print(f'{"Tabela 1":^15}')
print('')
while numero < 28:
    print(numero,end=' ')
    numero += 5
print(end ='\n')
print (40 * '=')

print(f'{"Tabela 2":^16}')
print('')
conta = 1.5
for c in range(0, 7):
    conta = (conta * 2) - 1
    print(f'{conta:.0f}', end = ' ')
print(end = '\n')
print(40 *'=')

print(f'{"Tabela 3":^12}')
print('')
for c in range(0, 5):
    conta2 = (3**c) + 1
    print(conta2, end = ' ')
print(end = '\n')
print(40 *'=')