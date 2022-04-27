numerador = int(input('Digite o numerador: '))
expoente = int(input('Digite o expoente: '))    
valor = numerador
for c in range(0, expoente - 1):
    numerador = numerador * valor
print(f'Oúmero {valor} elevado a {expoente} é igual a {numerador}.')