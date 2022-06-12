import random 
QTD_NAVIOS     = 7  
QTD_SUBMARINOS = 4   
QTD_POSTOS     = 5 
  
AGUA_NEV      = 0   
NAVIO_NEV     = 1   
SUBMARINO_NEV = 2   
POSTO_NEV     = 3   
NAVIO         = 4   
SUBMARINO     = 5   
POSTO         = 6  
AGUA_ATINGIDA = 7 
  
mar = []


def nomePiloto(): 
    try: 
        name = input('insira seu nome: ') 
        print('_' * (17 + len(name))) 
        print('Seu nome é', name) 
        print('    =========================================')        
    except ValueError: 
        print('Invalido') 
  
  
def iniciaMarInimigo(m): 
    for i in range(10): 
        lin = [] 
        for j in range(10): 
            lin.append(0) 
        m.append(lin) 
    posicionaElemento(NAVIO_NEV , QTD_NAVIOS) 
    posicionaElemento(SUBMARINO_NEV, QTD_SUBMARINOS) 
    posicionaElemento(POSTO_NEV , QTD_POSTOS) 

  
def posicionaElemento(tipo,q): 
    for nums in range(q): 
         while True:
            i = random.randint(0,9) 
            j = random.randint(0,9)  
            if mar[i][j] == 0:  
                mar[i][j] = tipo 
                break                
        
                                     
def tipoElemento(codigo): 
    if codigo == AGUA_NEV: 
        return '.' 
    if codigo == NAVIO_NEV: 
        return '.' 
    if codigo == SUBMARINO_NEV: 
        return '.' 
    if codigo == POSTO_NEV: 
        return '.' 
    elif codigo == NAVIO: 
        return 'N' 
    elif codigo == SUBMARINO: 
        return 'S'
    elif codigo == POSTO: 
        return 'P' 
    else: 
        return '%' 


def exibeMarInimigo(mar): 
    print('    ',end='')
    for i in range(10):
        print(f'|[{i}]',end='')
    print('|')    
    print('    +---+---+---+---+---+---+---+---+---+---+')    
    for i in range(10):  
        print(f"[{i}] |",end='')  
        for j in range(10):  
            simbolo = tipoElemento(mar[i][j])  
            print(f"{simbolo:^3}|",end='')  
        print("\n    +---+---+---+---+---+---+---+---+---+---+") 
 
nomePiloto() 
iniciaMarInimigo(mar) 
exibeMarInimigo(mar)