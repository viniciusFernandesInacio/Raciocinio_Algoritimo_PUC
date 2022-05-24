matriz = []

def criarMatriz1():
    global matriz
    ultimo = False
    matriz = [['.' for x in range(5)]]
    for lin, linhas in enumerate(matriz):
        for colu, coluna in enumerate(linhas):
            if not ultimo:
                matriz[lin][colu] = ' [*_*] '
                ultimo = True
            else:
                ultimo = False

def criarMatriz2():
    global matriz
    ultimo = False
    matriz = [['.' for x in range(5)]]
    for lin, linhas in enumerate(matriz):
        for colu, coluna in enumerate(linhas):
            if lin == colu:
                matriz[lin][colu] = " (^_^) "
            elif lin + colu == 4:
                matriz[lin][colu] = " [-_-]"

def printMatriz():
    print(matriz)

criarMatriz1()
printMatriz()
print('\n')
criarMatriz2()
printMatriz()
