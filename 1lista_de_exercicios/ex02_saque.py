saque = int(input("Qual o calor que você deseja sacar?"))
nota20 = saque // 20
nota5 = saque % 20 // 5
nota2 = saque % 20 // 2
nota1 = saque % 20 % 5 % 2 // 1
print("Você ira receber " + str(nota20) + " notas de 20, " + str(nota5) + " notas de cinco, " + str(nota2) + " notas de dois e " + str(nota1) + " notas de um.")