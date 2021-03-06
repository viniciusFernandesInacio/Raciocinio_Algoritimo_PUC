import random
import os

# ------ CONSTANTES ------
QTD_NAVIOS = 7
QTD_SUBMARINOS = 4
QTD_POSTOS = 5

AGUA_NEV = 0        #'.' Código e símbolo para água no nevoiro
NAVIO_NEV = 1       #'.' Código e símbolo para navio no nevoeiro
SUBMARINO_NEV = 2   #'.' Código e símbolo para submarino no nevoeiro
POSTO_NEV = 3       #'.' Código e símbolo para posto no nevoeiro
NAVIO = 4           #'N' Código e símbolo para navio atingido
SUBMARINO = 5       #'S' Código e símbolo para submarino atingido
POSTO = 6           #'P' Código e símbolo para posto atingido
AGUA_ATINGIDA = 7   #'%' Código e símbolo para água atingida

# ------ VARIÁVEIS GLOBAIS ------
mar_inimigo = []
disparos = []
nome = ""           #Nome do jogador
qtdD = 0            #Quantidade de disparo realizados
qtdN = 0            #Quantidade de navios atingidos
qtdS = 0            #Quantidade de submarinos atingidos
qtdD_temp = 0       #Quantidade temporária de disparos
msg = ""            #Mensagens que seram printadas na tela
total_pontos = 0    #Total de pontos conquistados
ret = 1             #Váriavel que consta se o jogo deve ser continuado ou não

def inicia_mar_inimigo():
    """
    Coloca todos os elementos do jogo atraves um Laço for aninhado que faz a chamada da função 'posiciona_elemento' várias vezes.
    """
    global mar_inimigo
    mar_inimigo = [[0 for x in range(10)]for y in range(10)]
    posiciona_elemento(NAVIO_NEV, QTD_NAVIOS)
    posiciona_elemento(POSTO_NEV, QTD_POSTOS)
    posiciona_elemento(SUBMARINO_NEV, QTD_SUBMARINOS)


def posiciona_elemento(estrutura, quantidade):
    """
    Posiciona os elementos na matriz 'mar_inimigo' esando coordenadas aleatórias
    Parâmetro 'estrutura': Elemento que será posicionado na matriz
    Parâmetro 'quantidade': Quantidade de elementos que seram colocados na matriz
    """
    for i in range(quantidade):
        while True:
            x = random.randint(0, 9)
            y = random.randint(0, 9)
            if mar_inimigo[y][x] == AGUA_NEV:
                mar_inimigo[y][x] = estrutura
                break


def tipo_elemento(codigo):
    """
    Atrela um código a um elemento grafico do jogo (EXEMPLO: O código pra água atingida é '7' e o elemento grafico é '%')
    Parâmetro código: Código das variaveis que teram elementos graficos atrelados a elas (as variáveis foram declaradas no inicio do código)
    """
    tipos = {AGUA_NEV: ".", NAVIO_NEV: ".", SUBMARINO_NEV: ".", POSTO_NEV: ".", NAVIO: "N", SUBMARINO: "S", POSTO: "P", AGUA_ATINGIDA: "%"}
    return tipos[codigo]


def exibir_mar_inimigo():
    """
    Imprime o mar inimigo no terminal. Ele acessa cada cada um dos valores (códigos) da matriz e atrela a eles seus respectivos elementos graficos. Tambem realiza a chamada da função 'tipo_elemento'
    """
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
    """
    Define o nome do jogador e logo após realiza a limpeza de dados do terminal
    """
    global nome
    while True:
        try:
            nome = input("Insira o nome do piloto: ")
            break
        except:
            print("Valor inválido, tente novamente!")
        os.system("cls" if os.name == "nt" else "clear")



def inicializa_jogo():
    """
    Inicializa o jogo realizando a limpeza da tela, declarando variáveis e atualizando a mensagem de início
    """
    os.system("cls" if os.name == "nt" else "clear")
    global ret
    global msg
    global qtdD
    global qtdN
    global qtdS
    global qtdD_temp
    global total_pontos
    global disparos
    ret = 1
    qtdD = 0
    qtdN = 0
    qtdS = 0
    qtdD_temp = 0
    total_pontos = 0
    disparos = []
    msg = "Início de jogo, boa sorte!"


def apresenta_tela():
    """
    Apresenta a tela chamando a função e imprime as variáveis relacionadas à pontuação
    """
    os.system("cls" if os.name == "nt" else "clear")
    exibir_mar_inimigo()
    print(f"Disparos realizados: {qtdD}")
    print(f"Navios atingidos: {qtdN}")
    print(f"Submarinos atingidos: {qtdS}")
    print(f"Total de pontos: {total_pontos}")
    print()
    print(msg)


def verifica_disparo(coordenada):
    """
    Verifica se a coordenada digitada pelo usuário bate com algum código, da a postuação e atribui o que o usuário o que ele atingiu à variavel da mensagem
    Parâmetro 'coordenada': Coordenadas do ultimo tiro do jogador (as coordenadas são coletadas usando a função 'pedir_coordenadas')
    """
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
    if mar_inimigo[coordenada[1]][coordenada[0]] == AGUA_NEV:
        msg = "Água atingida, realize outro disparo!"
        mar_inimigo[coordenada[1]][coordenada[0]] = AGUA_ATINGIDA
    elif mar_inimigo[coordenada[1]][coordenada[0]] == NAVIO_NEV:
        msg = "Návio atingido, realize outro disparo!"
        qtdN += 1
        total_pontos += 5
        mar_inimigo[coordenada[1]][coordenada[0]] = NAVIO
    elif mar_inimigo[coordenada[1]][coordenada[0]] == SUBMARINO_NEV:
        msg = "Submarino atingido, realize outro disparo!"
        qtdS += 1
        total_pontos += 7
        mar_inimigo[coordenada[1]][coordenada[0]] = SUBMARINO
    elif mar_inimigo[coordenada[1]][coordenada[0]] == POSTO_NEV:
        mar_inimigo[coordenada[1]][coordenada[0]] = POSTO
        msg = "Posto atingido, fim de jogo!"
        return 0
    if qtdN == QTD_NAVIOS and qtdS == QTD_SUBMARINOS:
        msg = "Todos os navios e submarinos foram atingidos, fim de jogo!"
        return 0


def jogo():
    """
    Realiza o inicio do jogo pedindo as coordenadas do primeiro tiro chamando a função 'pedir_coordenadas'
    """
    def pedir_coordenada():
        """
        Função aninhada que pede coordenadas ao usuário e a retorna para ser usada como parâmetro na função verifica_disparo
        :return:
        """
        global disparos
        while True:
            disparo_t = []
            try:
                x = int(input("Insira uma coordenada de X para realizar o disparo: "))
                y = int(input("Insira uma coordenada de Y para realizar o disparo: "))
            except ValueError:
                print("Valor inválido, tente novamente!")
                continue
            if 0 <= x <= 9 and 0 <= y <= 9:
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

    global ret
    inicializa_jogo()
    inicia_mar_inimigo()
    nome_piloto()
    while True:
        apresenta_tela()
        ret = verifica_disparo(pedir_coordenada())
        if ret == 0:
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
