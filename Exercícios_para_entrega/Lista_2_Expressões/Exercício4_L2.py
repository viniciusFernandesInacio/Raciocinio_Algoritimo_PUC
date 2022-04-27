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