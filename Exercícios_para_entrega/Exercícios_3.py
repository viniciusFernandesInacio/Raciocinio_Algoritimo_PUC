#EXERCÍCIO 01:
'''import sys


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
print(f'Você digitou {par} números pares e {impar} números ímpares.')'''


#EXERCÍCIO 02:
'''for c in range(0,5):
    res = float(input(f'Digite o {c + 1}º número: '))
    if (c == 0):
        maior = res
        menor = res
    if (c > 0):
        if (res > maior):
             maior = res
        if (res < menor):
            menor =    res
print(40 * '=')
print(f'O maior número digitado foi {maior}.\nO menor número digitado foi {menor}.')
print(40 * '=')'''


#EXERCÍCIO 03:
'''res = int(input('Digite um número para o calculo da tabuada: '))
for c in range(0,10):
    c = c + 1
    print(f'{res} x {c} = {res * c}')'''


#EXERCÍCIO 04:
'''numerador = int(input('Digite o numerador: '))
expoente = int(input('Digite o expoente: '))    
valor = numerador
for c in range(0, expoente - 1):
    numerador = numerador * valor
print(f'Oúmero {valor} elevado a {expoente} é igual a {numerador}.')'''    


#EXERCÍCIO 05:
'''while True:
    login = input('LOGIN: ')
    senha = input('SENHA: ')
    if (login == 'vinicius') and (senha == 'fernandes'):
        print('Bem-vindo ao sistema!')
        break
    else:
        print('[ERRO] Login ou senha incorrretos!') 
        break'''


#EXERCÍCIO 06:
'''soma = 0
cont = 0
print('=' * 40)
while True:
    res = float(input(f'Informe o {cont + 1} número (Digite 0 para parar a contagem).\n--> '))
    if res == 0:
        break
    soma = soma + res
    cont += 1
print('=' * 40)
print(f'A média de todos os valoeres é {soma / cont:.2f}')'''    


#EXERCÍCIO 07:
'''num1 = 1
num2 = 1
total = 0
tudo = ''
escolha = int(input('Informe um número: '))
if escolha == 1:
    print(f'Os valores de Fibonacci menores que {escolha} são: 0')
if escolha == 2:
    print(f'Os valores de Fibonacci menores que {escolha} são: 0 0 1')
while escolha > total:
    total = num1 + num2
    if total >= escolha:
        break
    num2 = num1
    num1 = total
    tudo += str(total)
    tudo += ' '
if escolha > 2:
    print(f'Os valores de Fibonacci menores que {escolha} são: 0 1 1 {tudo}.')'''


#EXERCÍCIO 08:        
'''numero = 2
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
print(40 *'=')'''


print(f'{"Carinnho de compras":^30}')
print(30 * '=')
soma = 0
total = 0
while True:
    name = str(input('Informe o nome do produto:'))
    value_product = float(input('Informe o valor do produto:'))
    amount = float(input('Informe a quantidade que deseja:'))
    question = str(input('Deseja adicionar algo mais[S/N]:')).upper()[0]
    print(30 * '=')
    soma = value_product * amount
    total = total + soma
    if question == 'N':
        break
print(f'O preço total das compras será de R${total:.2f}')