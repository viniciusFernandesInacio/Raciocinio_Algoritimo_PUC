print(40 * "=")
print("Caulculo Para a Média de Temperatura")
print(40 * "=")
mes = ["Janeiro","Fevereiro","Março","Abriu","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"]
l_temp = []
soma = 0
acima = []
for i in range(12):
    temp = float(input(f"A temperatura média no mês de {mes[i]} foi de (°C):"))
    l_temp.append(temp)
    soma += temp
media = soma / 12
for c in range (12):
    if(l_temp[c] > media):
        acima.append(mes[c])
print(f"A média anual de temperatura foi de {media}°C.")
print(f"Os meses que tiveram a temperatura acima da média foram: {acima}")             