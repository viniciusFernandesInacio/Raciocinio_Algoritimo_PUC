print(40 * "=")
print("Caulculo da Média\nVerificação de Valores\n\nDigite os valores abaixo.")
maior = []
menor = []
igual = []
vet = []
soma = 0
for i in range(6):
    num = int(input(f"Insira o {i + 1}º número para o caulculo da média --> "))
    soma += num
    vet.append(num)
media = soma / 6
for c in range(6):
    if(vet[c] > media):
        maior.append(vet[c])
    elif(vet[c] < media):
        menor.append(vet[c])
    else:
        igual.append(vet[c])
print(f"A média dos números inseridos é {media}.")                    
print(f"Os números abaixo da média são: {menor}.")                    
print(f"Os números acima da média são: {maior}.")                    
print(f"Os números iguais a média são: {igual}")                    