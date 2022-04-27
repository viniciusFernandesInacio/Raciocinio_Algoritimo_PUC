produto = input("Qual é o produto?\n--> ")
preço_custo = float(input("Qual o preço de custo do produto?\n--> "))
acrescimo = preço_custo * 0.30
preço_final = preço_custo + acrescimo
print("O valor final do " + str(produto) + " é de R$" + str(preço_final))