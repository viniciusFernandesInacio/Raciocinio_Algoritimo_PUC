'''anoatual = 2022
anonasc = int(input("Em que ano você nasceu? "))
idade = anoatual - anonasc
resp = (str(input("Você ja fez aniversario esta ano? ")))
if (resp == "não"):
    idade = idade - 1
print("Sua idade é " + str(idade)) '''


'''print("Escreva um número entre 0 e 10 :")
numero = int(input("Número:"))
if (numero >= 5):
    print("Número maior que 5.")
else:
    print("Número menor que 5.")'''


'''print("Digite quatro notas da sua diciplina: ")
nota1 = float(input("Primeira nota: "))        
nota2 = float(input("Segunda nota: "))        
nota3 = float(input("Terceira nota: "))        
nota4 = float(input("Quarta nota: "))
media = (nota1 + nota2 + nota3 + nota4) / 4
print("Sua nota média foi de " + str(media) + ".")
if (media > 70):
    print("Você esta na média.")
elif (media >= 40):
    print("Você esta de recuperação.")
else:
    print("Reprovado.50")'''      


'''print("Digite três números diferentes: ")
num1 = float(input("Primeiro número: "))
num2 = float(input("Segundo número: "))
num3 = float(input("Terceiro número: "))
if (num1 < num2) and (num2 < num3):
    print("O primeiro número é o menor.")
elif (num2 < num1) and (num2 < num3):
    print("O segundo número é o menor.")
else:
    print("O terceiro número é menor.")'''


'''numero = int(input("Digite um numero qualquer: "))
if (numero % 2 == 0):
    print("O número é par")
else:
    print("Número impar")'''



'''num = int(input("Digite um número qualquer: "))
if(num > -3 and num < 12):
    print("O número " + str(num) + " esta no intervalo entre -3 e 12.")
else:
    print("O número " + str(num) + " não se encontra no intervalo entre -3 e 12")'''


'''peso = float(input("Qual o peso do boxeador? \n--> ")) 
if (peso < 50):
    print("Peso palha.")
elif (peso >= 50) and (peso < 59.99):
    print("Peso pluma.")     
elif (peso >= 60) and (peso < 75.99):
    print("Peso leve.")     
elif (peso >= 76) and (peso < 87.99):
    print("Peso pesado.")
else:
    print("Peso super pesado.")'''

#Valores das retas
'''valor_a = float(input("Qual o tamanho da primira linha?\n-->"))        
valor_b = float(input("Qual o tamanho da segunda linha?\n-->"))        
valor_c = float(input("Qual o tamanho da terceira linha?\n-->")) 

#Teste triangulos
if(valor_a + valor_b > valor_c) and (valor_a + valor_c > valor_b) and (valor_c + valor_b):
    if (valor_a == valor_b) and (valor_b == valor_c):
        print("O triângulo é equilatero.")
    elif (valor_a == valor_b) or (valor_a == valor_b) or (valor_b == valor_c):
        print("O triângulo é isócelis")           
    else:
        print("O triângulo é escaleno.")
else:
    print("Não é um triâgulo!")'''  



