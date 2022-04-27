salario = 1820.00
nome = input("Qual o nome do vendedor? \n--> ")
carros = int(input("Quantos carros foram vendidos? \n--> "))
comissao_fixa = carros * 50
comissao_vari = (carros * 30000) * 0.5
salario_final = salario + comissao_fixa + comissao_vari
print(nome + " vendeu " + str(carros) + " carros e irá receber o salário de $" + str(salario_final))