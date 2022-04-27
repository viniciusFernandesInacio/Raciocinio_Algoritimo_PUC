print(30 * "--")
print('Equação do segundo grau.')
print(30 * "--")
print('Seja a equanção do segundo grau: Ax**2+Bx+C')
a = int(input('Insira o valor de A: '))
b = int(input('Insira o valor de B: '))
c = int(input('Insira o valor de C: '))
delta = b ** 2 - 4 * a * c
if (a == 0):
    print('Não é uma equação do segundo grau!')
elif (delta < 0):
    print('Não possui raizes reais!')    
elif (delta == 0):
    print('Possui uma raiz real!')
    x = (- b + (delta ** 0.5)) / (2 * a)
    print('x = ', x)
else:
    x1 = (- b + (delta ** 0.5)) / (2 * a)        
    x2 = (- b - (delta ** 0.5)) / (2 * a)
    print('x1 = {0:2.2f} e x2 = {1:2.2f}'.format(x1, x2))