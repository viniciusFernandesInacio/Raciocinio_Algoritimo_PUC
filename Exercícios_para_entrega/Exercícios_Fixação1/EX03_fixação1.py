nome = input("Qual o nome do vendedor?\n--> ")
salario_fixo = float(input("Qual o salário fixo do " + nome + "?\n--> "))
vendas = float(input("Qual foi o total de vendas?\n--> "))
comissao = vendas * 0.15
salario_tot = salario_fixo + comissao
print(nome + " seu salário fixo é de " + str(salario_fixo) + " e seu salário total é de " + str(salario_tot) + "!")