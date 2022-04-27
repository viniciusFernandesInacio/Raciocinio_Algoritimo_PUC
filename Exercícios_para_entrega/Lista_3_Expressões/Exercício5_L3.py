'''Elabore um programa que o valor da série S abaixo. Considere que o valor inteiro de n = 5. Faça o 
TESTE DE MESA.'''

s = 0
for c in range(1, 6):
    s += ((2*c) - 1)/(3*c)
print(s)