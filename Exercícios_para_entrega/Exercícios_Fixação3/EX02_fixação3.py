for c in range(0,5):
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
print(40 * '=')