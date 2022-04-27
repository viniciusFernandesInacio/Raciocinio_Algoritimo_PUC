num1 = 1
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
    print(f'Os valores de Fibonacci menores que {escolha} são: 0 1 1 {tudo}.')