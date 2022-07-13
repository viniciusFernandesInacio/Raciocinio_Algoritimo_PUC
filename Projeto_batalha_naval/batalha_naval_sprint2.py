import random
import os

# ------ CONSTANTES ------
qtd_navios = 1
qtd_submarinos = 1
qtd_postos = 1

agua_nev = 0        #'.' Código e símbolo para água no nevoiro
navio_nev = 1       #'.' Código e símbolo para navio no nevoeiro
submarino_nev = 2   #'.' Código e símbolo para submarino no nevoeiro
posto_nev = 3       #'.' Código e símbolo para posto no nevoeiro
navio = 4           #'N' Código e símbolo para navio atingido
submarino = 5       #'S' Código e símbolo para submarino atingido
posto = 6           #'P' Código e símbolo para posto atingido
agua_atingida = 7   #'%' Código e símbolo para água atingida

# ------ VARIÁVEIS GLOBAIS ------
mar_inimigo = []
disparos = []
nome = ""           #Nome do jogador
qtdD = 0            #Quantidade de disparo realizados
qtdN = 0            #Quantidade de navios atingidos
qtdS = 0            #Quantidade de submarinos atingidos
qtdD_temp = 0       #Quantidade temporaria de disparos
msg = ""            #Mensagens que seram printadas na tela
total_pontos = 0    #Total de pontos conquistados

def inicia_mar_inimigo():
    """
    Coloca todos os elementos do jogo atraves um Laço for aninhado que faz a chamada da função 'posiciona_elemento' várias vezes.
    """
    global mar_inimigo
    mar_inimigo = [[0 for x in range(10)]for y in range(10)]
    posiciona_elemento(navio_nev, qtd_navios)
    posiciona_elemento(posto_nev, qtd_postos)
    posiciona_elemento(submarino_nev, qtd_submarinos)


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
            if mar_inimigo[y][x] == 0:
                mar_inimigo[y][x] = estrutura
                break


def tipo_elemento(codigo):
    """
    Atrela um código a um elemento grafico do jogo (EXEMPLO: O código pra água atingida é '7' e o elemento grafico é '%')
    Parâmetro código: Código das variaveis que teram elementos graficos atrelados a elas (as variáveis foram declaradas no inicio do código)
    """
    tipos = {0: ".", 1: "n", 2: "s", 3: "p", 4: "N", 5: "S", 6: "P", 7: "%"}
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
    if qtdN == qtd_navios and qtdS == qtd_submarinos:
        msg = "Todos os navios e submarinos foram atingidos, fim de jogo!"
        return "fim"


def jogo():
    """
    Realiza o inicio do jogo pedindo as coordenadas do primeiro tiro chamando a função 'pedir_coordenadas'
    """
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