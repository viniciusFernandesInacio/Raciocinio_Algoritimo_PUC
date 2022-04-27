peso = float(input("Qual o peso do boxeador? \n--> ")) 
if (peso < 50):
    print("Peso palha.")
elif (peso >= 50) and (peso < 59.99):
    print("Peso pluma.")     
elif (peso >= 60) and (peso < 75.99):
    print("Peso leve.")     
elif (peso >= 76) and (peso < 87.99):
    print("Peso pesado.")
else:
    print("Peso super pesado.")