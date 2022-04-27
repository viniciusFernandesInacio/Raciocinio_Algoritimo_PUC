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