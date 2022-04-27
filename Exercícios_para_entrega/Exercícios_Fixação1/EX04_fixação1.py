nome = input("Qual o nome do aluno?\n--> ")
nota_1 = float(input("Qual foi a primeira nota?\n--> "))
nota_2 = float(input("Qual foi a segunda nota?\n--> "))
nota_3 = float(input("Qual foi a terceira nota?\n--> "))
media = (nota_1 + nota_2 + nota_3) // 3
print("A média final do aluno(a) " + nome + " foi de " + str(media) + "!")