#Algoritimo que diz se um número é par ou impar:
'''numero = int(input("Digite um numero qualquer: "))
if (numero % 2 == 0):
    print("O número é par")
else:
    print("Número impar")'''


#Algoritimo que diz se um número está no intervalo entre -3 e 12: 
'''num = int(input("Digite um número qualquer: "))
if(num > -3 and num < 12):
    print("O número " + str(num) + " esta no intervalo entre -3 e 12.")
else:
    print("O número " + str(num) + " não se encontra no intervalo entre -3 e 12")'''


#Algoritimo que diz a categoria de um boxeador:
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
valor_c = float(input("Qual o tamanho da terceira linha?\n-->"))''' 

#Teste triangulos
'''if(valor_a + valor_b > valor_c) and (valor_a + valor_c > valor_b) and (valor_c + valor_b):
    if (valor_a == valor_b) and (valor_b == valor_c):
        print("O triângulo é equilatero.")
    elif (valor_a == valor_b) or (valor_a == valor_b) or (valor_b == valor_c):
        print("O triângulo é isócelis")           
    else:
        print("O triângulo é escaleno.")
else:
    print("Não é um triâgulo!")'''


#Algorimo que calcula os descontos de uma loja:
import sys


calça = 89.90 #Masculino e feminino
blusa = 24.90 #Feminino
saia = 39.90 #Feminino
camisa = 49.50 #Masculino
vestido = 79.90 #Feminino
peça = input("Qual peça você deseja comprar?\n1.Calça\n2.Blusa\n3.Saia\n4.Camisa\n5.Vestido\n--> ")
if(peça == '1'):
    sexo = input('Modelo masculino ou feminino?\n1.Masculino  -  2.Feminino\n--> ')
    if(sexo == '1'):
        valor = calça * 0.8
    elif(sexo == '2'):
        valor = calça * 0.85  
    else:
        print('[ERRO]')
        sys.exit(0)
elif(peça == '2'):
    valor = blusa * 0.8        
elif(peça == '3'):     
    valor = saia * 0.8   
elif(peça == '4'):    
    valor = camisa * 0.85    
elif(peça == '5'):       
    valor = vestido * 0.8
else:
    sys.exit(0)   
f_pagamento = input('Qual a sua forma de pagamento?\n1.Dinheiro  /  2.Cartão\n--> ')      
if(f_pagamento == '1'):
    valor *= 0.95
elif(f_pagamento == '2'):
    valor *= 1.05
else:
    print('[ERRO]')
    sys.exit(0)
print('O valor a pagar é de R$' + str(valor))            
