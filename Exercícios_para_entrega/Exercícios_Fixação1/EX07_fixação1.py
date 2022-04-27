cotaçao = float(input("Qual a cotação atual do dolar?\n--> "))
dolares = float(input("Quantos dolares você tem?\n--> "))
reais = dolares / cotaçao
print("O valor de $" + str(dolares) + " convertidos para reais fica R$" + str(reais))