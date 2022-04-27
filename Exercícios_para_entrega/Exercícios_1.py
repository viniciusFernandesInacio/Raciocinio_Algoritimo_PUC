#Exercício 1: Algoritimo que mostra a soma, subtração, divisão e multiplicação entre dois números:
'''num_1 = float(input("Digite o primeiro número:\n--> "))
num_2 = float(input("Digite o segundo número:\n--> "))
res_soma = num_1 + num_2
res_sub = num_1 - num_2
res_div = num_1 / num_2
res_mult = num_1 * num_2
print("* A soma dos números é: " + str(res_soma) + "\n* A subtração dos números é igual a " + str(res_sub) + "\n* A divisão dos números é igual a " + str(res_div) + "\n* A multiplicação dos números é igual a " + str(res_mult))'''


#Exercicio 2: Algoritimo que diz o consumo médio de um veículo durante uma viagem:
'''dist_per = float(input("Digite a distância total percorrida pelo veículo:\n--> "))
combus_gasto = float(input("Digite o total de combustível gasto na viagem:\n--> "))
consumo_med = dist_per / combus_gasto
print("O seu gasto médio de combustível foi de " + str(consumo_med) + "!")'''


#Exercício 3: Algoritimo que calcula o sálario de um funcionário juntamente com a comissão:
'''nome = input("Qual o nome do vendedor?\n--> ")
salario_fixo = float(input("Qual o salário fixo do " + nome + "?\n--> "))
vendas = float(input("Qual foi o total de vendas?\n--> "))
comissao = vendas * 0.15
salario_tot = salario_fixo + comissao
print(nome + " seu salário fixo é de " + str(salario_fixo) + " e seu salário total é de " + str(salario_tot) + "!")'''


#Execício 4: Algoritimo para informar a nota média de um aluno:
'''nome = input("Qual o nome do aluno?\n--> ")
nota_1 = float(input("Qual foi a primeira nota?\n--> "))
nota_2 = float(input("Qual foi a segunda nota?\n--> "))
nota_3 = float(input("Qual foi a terceira nota?\n--> "))
media = (nota_1 + nota_2 + nota_3) // 3
print("A média final do aluno(a) " + nome + " foi de " + str(media) + "!")'''

#Exercício 5: Algoritimo que efetua a troca de dois valores:
'''valor_a = input("Digite o valor de A:\n--> ")
valor_b = input("Digite o valor de B: \n--> ")
valor_c = valor_a
valor_a = valor_b
valor_b = valor_c
print("O valor de A após trocado é de '" + valor_a + "' e o valor de B após trocado é de '" + valor_b + "'.")'''


#Exercício 6: Algoritimo que converte uma temperatura de Celsius para Fahrenheit:
'''temp_c = float(input("Digite a temperatura em celsius:\n--> "))
temp_f = (9 * temp_c + 160) / 5
print("A temperatura convertida para Fahrenheit fica: " + str(temp_f) + "!")'''


#Exercício 7: Algoritimo que converte um valor em dolar para real:
'''cotaçao = float(input("Qual a cotação atual do dolar?\n--> "))
dolares = float(input("Quantos dolares você tem?\n--> "))
reais = dolares / cotaçao
print("O valor de $" + str(dolares) + " convertidos para reais fica R$" + str(reais))'''


#Exercício 8: Algoritimo que mostra o parcelamento de um produto:
'''produto = input("Qual dos seguintes produtos você irá levar?\n--> ")
valor = float(input("Qual o valor do produto?\n--> "))
parcelas = valor / 5
print("A nossa promoçâo para parcelamento e cinco vezes sem juros para " + produto + " fica num total de cinco parcelas no valor de R$" + str(parcelas))'''


#Exercício 9: Algoritimo para receber o preço de custo de um produto e aumentar sseu valor:
'''produto = input("Qual é o produto?\n--> ")
preço_custo = float(input("Qual o preço de custo do produto?\n--> "))
acrescimo = preço_custo * 0.30
preço_final = preço_custo + acrescimo
print("O valor final do " + str(produto) + " é de R$" + str(preço_final))'''


#Exercício 10: Algoritimo que le o valor de fabrica de um veículo e retorna o valor com os impostos:
valor_fabrica = float(input("Qual o valor de fabrica do veículo?\n--> "))
perc_distribuidor = valor_fabrica * 0.28
impostos = valor_fabrica * 0.45
valor_final = valor_fabrica + perc_distribuidor + impostos
print("O valor final do veículo é de R$" + str(valor_final))
