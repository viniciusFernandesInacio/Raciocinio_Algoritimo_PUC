#Exercício 1:
'''print(30 * "--")
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
    print('x1 = {0:2.2f} e x2 = {1:2.2f}'.format(x1, x2))'''       


#Exercício 2:
'''import sys


num = {
    0: 'Zero',
    1: 'Um',
    2: 'Dois',
    3: 'Três',
    4: 'Quatro',
    5: 'Cinco',
    6: 'Seis',
    7: 'Sete',
    8: 'Oito',
    9: 'Nove'
}
opçao = int(input('Digite um número com apenas um algarismo:\n--> '))
if(opçao > 9):
    print('[ERRO]')
    sys.exit(0)
elif(opçao >= 0) and (opçao < 10):
    print(num.get(opçao))
else:
    print('[ERRO]')
    sys.exit(0)'''


#Exercício 3:
'''mes = {
    1: 'Janeiro',
    2: 'Fevereiro',
    3: 'Março',
    4: 'Abril',
    5: 'Maio',
    6: 'Junho',
    7: 'Julho',
    8: 'Agosto',
    9: 'Setembro',
    10: 'Outubro',
    11: 'Novembro',
    12: 'Dezembro'
}
opçao = int(input('1.Janeiro\n2.Feverreiro\n3.Março\n4.Abril\n5.Maio\n6.Junho\n7.Julho\n8.Agosto\n9.Setembro\n10.Outubro\n11.Novembro\n12.Dezembro\nDigite um número correspondente a um mês: '))
if(opçao > 0) and (opçao < 13):
    print(mes.get(opçao))
else:
    print('[ERRO] Você não escolheu um número correspondente a um mês.')'''

#Exercício 4:
import sys


mes_nome = {
    1: 'Janeiro',
    2: 'Fevereiro',
    3: 'Marça',
    4: 'Abril',
    5: 'Maio',
    6: 'Junho',
    7: 'Julho',
    8: 'Agosto',
    9: 'Setembro',
    10: 'Outubro',
    11: 'Novembro',
    12: 'Dezembro'
}
mes_dias = {
    1: '31',
    2: '29',
    3: '31',
    4: '30',
    5: '31',
    6: '30',
    7: '31',
    8: '31',
    9: '30',
    10: '31',
    11: '30',
    12: '31'
}
res_mes = int(input('Escolha um mês (1 a 12): '))
ano = int(input('Digite um ano (4 digitos): '))
if(ano % 4 == 0) and (ano == 2):
    res_mes += 1
if(res_mes > 0) and (res_mes < 13):
    mes = mes_nome.get(res_mes)
    dias = mes_dias.get(res_mes)
    print('Mês escolhido:[' + str(mes) + '], com [' + str(dias) + '] dias no ano de [' + str(ano) + '].')
else:
    print('[ERRRO]')
    sys.exit(0)    