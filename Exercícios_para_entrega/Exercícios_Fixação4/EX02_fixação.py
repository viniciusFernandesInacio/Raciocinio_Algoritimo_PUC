print(40 * "=")
print("Misturando listas e intercalando elementos.")
print(40 * "=")
lista_1 = []
lista_2 = []
lista_3 = []
for i in range(5):
    x = int(input(f"Insira 0 {i + 1}º elemento da segunda lista:"))
    lista_1.append(x)
print("\n")    
for c in range(5):
    y = int(input(f"Insira 0 {c + 1}º elemento da segunda lista:"))
    lista_2.append(y)
print("\n")   
for cont in range(5):
    lista_3.append(lista_1[cont])
    lista_3.append(lista_2[cont])
print(f"Os elementos da primeira lista são: {lista_1}.")    
print(f"Os elementos da segunda lista são: {lista_2}.")    
print(f"Os elementos das duas listas intercaladas são: {lista_3}.")    