import os
# EXEMPLO COM TRATAMENTO DE EXCEÇÃO PARA AS ENTRADAS DE DADOS
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

continuar = True
item = 0
totalCompra = 0
while continuar:
    compra = 0
    while True:
        cls()
        nome = str(input("Entre com o nome do Produto: "))
        if (nome == ""):
            print("  -- Nome do produto não pode ser vazio.")
            print("  -- Digite <ENTER> para continuar.")
            input()
        else:
            break


    while True:
        cls()
        try:
            valor = float(input(f"Entre com o valor do Produto [{nome}]: "))
            if (valor < 0):
                print("  -- Valor do produto não pode ser negativo.")
                print("  -- Digite <ENTER> para continuar.")
                input()
            else:
                break    
        except ValueError:
            print("  -- Valor do produto tem que ser um número real.")
            print("  -- Digite <ENTER> para continuar.")
            input()
        except:
            print("  -- Erro de digitação.")
            print("  -- Digite <ENTER> para continuar.")
            input()


    while True:
        cls()
        try:
            qtd = int(input(f"Entre com a quantidade do Produto [{nome}] que custa [R${valor:.2f}]: "))
            if (qtd < 0):
                print("  -- Quantidade do produto não pode ser negativa.")
                print("  -- Digite <ENTER> para continuar.")
                input()
            else:
                break    
        except ValueError:
            print("  -- Quantidade do produto tem que ser um número inteiro.")
            print("  -- Digite <ENTER> para continuar.")
            input()
        except:
            print("  -- Erro de digitação.")
            print("  -- Digite <ENTER> para continuar.")
            input()

    compra += valor * qtd
    item   += 1
    totalCompra +=compra

    print('-'*40)
    print(f"Item ({item}) \n . Produto = {nome} \n . Valor  = R$ {valor:.2f} \n . Qtde = {qtd} \n ")
    print(f"Total = R$ {compra:.2f}")
    print('-'*40)

    resp = input("Deseja incluir mais itens no carrinho (s/n):")
    if (resp == 'n'):
        continuar = False

print("\n")
print("="*40)
print(f"Total final da compra = R$ {totalCompra:.2f}")
print("="*40)