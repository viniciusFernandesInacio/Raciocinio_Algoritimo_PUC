import random
import os

mar_inimigo = []
agua_nev = 0
navio_nev = 1
submarino_nev = 2
posto_nev = 3
navio = 4
submarino = 5
posto = 6
agua_atingida = 7
qtd_navios = 7
qtd_submarinos = 4
qtd_postos = 5
nome = ""
qtdD = 0
qtdN = 0
qtdS = 0
total_pontos = 0
disparos = []
qtdD_temp = 0
msg = ""


def inicia_mar_inimigo():
    global mar_inimigo
    mar_inimigo = [[0 for x in range(10)]for y in range(10)]
    posiciona_elemento(navio_nev, qtd_navios)
    posiciona_elemento(posto_nev, qtd_postos)
    posiciona_elemento(submarino_nev, qtd_submarinos)


def posiciona_elemento(estrutura, quantidade):
    for i in range(quantidade):
        while True:
            x = random.randint(0, 9)
            y = random.randint(0, 9)
            if mar_inimigo[y][x] == 0:
                mar_inimigo[y][x] = estrutura
                break


def tipo_elemento(codigo):
    tipos = {0: ".", 1: ".", 2: ".", 3: ".", 4: "N", 5: "S", 6: "P", 7: "%"}
    return tipos[codigo]


def exibir_mar_inimigo():
    for i in range(65):
        print("=", end="")
    print()
    print(f"                    Átaque Aéreo - Piloto: {nome}")
    for i in range(65):
        print("=", end="")
    print()
    print(f"     ", end="")
    for i in range(10):
        print(f" [{i}]  ", end="")
    print("\n    +-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+")
    for i in range(10):
        print(f"[{i}] |", end="")
        for j in range(10):
            simbolo = tipo_elemento(mar_inimigo[i][j])
            print(f"  {simbolo}  |", end="")
        print("\n    +-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+")
    print()


def nome_piloto():
    global nome
    while True:
        try:
            nome = input("Insira o nome do piloto: ")
        except ValueError:
            print("Valor inválido, tente novamente!")
        finally:
            os.system("cls" if os.name == "nt" else "clear")
            break


def inicializa_jogo():
    os.system("cls" if os.name == "nt" else "clear")
    global msg
    global qtdD
    global qtdN
    global qtdS
    global qtdD_temp
    global total_pontos
    global disparos
    qtdD = 0
    qtdN = 0
    qtdS = 0
    qtdD_temp = 0
    total_pontos = 0
    disparos = []
    msg = "Início de jogo, boa sorte!"


def apresenta_tela():
    os.system("cls" if os.name == "nt" else "clear")
    exibir_mar_inimigo()
    print(f"Disparos realizados: {qtdD}")
    print(f"Navios atingidos: {qtdN}")
    print(f"Submarinos atingidos: {qtdS}")
    print(f"Total de pontos: {total_pontos}")
    print()
    print(msg)


def verifica_disparo(coordenada):
    global qtdD
    global qtdN
    global qtdS
    global qtdD_temp
    global total_pontos
    global disparos
    global msg
    qtdD += 1
    qtdD_temp += 1
    if qtdD_temp == 5:
        total_pontos -= 1
        qtdD_temp = 0
    if mar_inimigo[coordenada[1]][coordenada[0]] == agua_nev:
        msg = "Água atingida, realize outro disparo!"
        mar_inimigo[coordenada[1]][coordenada[0]] = agua_atingida
    elif mar_inimigo[coordenada[1]][coordenada[0]] == navio_nev:
        msg = "Návio atingido, realize outro disparo!"
        qtdN += 1
        total_pontos += 5
        mar_inimigo[coordenada[1]][coordenada[0]] = navio
    elif mar_inimigo[coordenada[1]][coordenada[0]] == submarino_nev:
        msg = "Submarino atingido, realize outro disparo!"
        qtdS += 1
        total_pontos += 7
        mar_inimigo[coordenada[1]][coordenada[0]] = submarino
    elif mar_inimigo[coordenada[1]][coordenada[0]] == posto_nev:
        mar_inimigo[coordenada[1]][coordenada[0]] = posto
        msg = "Posto atingido, fim de jogo!"
        return "fim"


def jogo():
    def pedir_coordenada():
        global disparos
        while True:
            disparo_t = []
            try:
                x = int(input("Insira uma coordenada de X para realizar o disparo: "))
                y = int(input("Insira uma coordenada de Y para realizar o disparo: "))
            except ValueError:
                print("Valor inválido, tente novamente!")
                continue
            if 0 <= x <= 9:
                disparo_t.append(x)
                disparo_t.append(y)
            else:
                print("Valores inválidos, tente novamente!")
                continue
            if disparo_t in disparos:
                print("Coordenada já atingida, escolha outra!")
                continue
            disparos.append(disparo_t)
            return disparo_t

    inicializa_jogo()
    inicia_mar_inimigo()
    nome_piloto()
    while True:
        apresenta_tela()
        if verifica_disparo(pedir_coordenada()) == "fim":
            apresenta_tela()
            reiniciar = input("Gostaria de reiniciar o jogo? (s/n) ")
            if reiniciar == "s":
                inicializa_jogo()
                inicia_mar_inimigo()
                nome_piloto()
                continue
            elif reiniciar == "n":
                break
            else:
                print("Resposta inválida, tente novamente!")


jogo()