valor_a = float(input("Qual o tamanho da primira linha?\n-->"))        
valor_b = float(input("Qual o tamanho da segunda linha?\n-->"))        
valor_c = float(input("Qual o tamanho da terceira linha?\n-->"))

if(valor_a + valor_b > valor_c) and (valor_a + valor_c > valor_b) and (valor_c + valor_b):
    if (valor_a == valor_b) and (valor_b == valor_c):
        print("O triângulo é equilatero.")
    elif (valor_a == valor_b) or (valor_a == valor_b) or (valor_b == valor_c):
        print("O triângulo é isócelis")           
    else:
        print("O triângulo é escaleno.")
else:
    print("Não é um triâgulo!")