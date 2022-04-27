import sys


calça = 89.90 #Masculino e feminino
blusa = 24.90 #Feminino
saia = 39.90 #Feminino
camisa = 49.50 #Masculino
vestido = 79.90 #Feminino
peça = input("Qual peça você deseja comprar?\n1.Calça\n2.Blusa\n3.Saia\n4.Camisa\n5.Vestido\n--> ")
if(peça == '1'):
    sexo = input('Modelo masculino ou feminino?\n1.Masculino  -  2.Feminino\n--> ')
    if(sexo == '1'):
        valor = calça * 0.8
    elif(sexo == '2'):
        valor = calça * 0.85  
    else:
        print('[ERRO]')
        sys.exit(0)
elif(peça == '2'):
    valor = blusa * 0.8        
elif(peça == '3'):     
    valor = saia * 0.8   
elif(peça == '4'):    
    valor = camisa * 0.85    
elif(peça == '5'):       
    valor = vestido * 0.8
else:
    sys.exit(0)   
f_pagamento = input('Qual a sua forma de pagamento?\n1.Dinheiro  /  2.Cartão\n--> ')      
if(f_pagamento == '1'):
    valor *= 0.95
elif(f_pagamento == '2'):
    valor *= 1.05
else:
    print('[ERRO]')
    sys.exit(0)
print('O valor a pagar é de R$' + str(valor))