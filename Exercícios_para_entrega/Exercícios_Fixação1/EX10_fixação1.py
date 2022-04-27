valor_fabrica = float(input("Qual o valor de fabrica do veículo?\n--> "))
perc_distribuidor = valor_fabrica * 0.28
impostos = valor_fabrica * 0.45
valor_final = valor_fabrica + perc_distribuidor + impostos
print("O valor final do veículo é de R$" + str(valor_final))