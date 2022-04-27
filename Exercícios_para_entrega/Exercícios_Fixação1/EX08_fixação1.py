produto = input("Qual dos seguintes produtos você irá levar?\n--> ")
valor = float(input("Qual o valor do produto?\n--> "))
parcelas = valor / 5
print("A nossa promoçâo para parcelamento e cinco vezes sem juros para " + produto + " fica num total de cinco parcelas no valor de R$" + str(parcelas))