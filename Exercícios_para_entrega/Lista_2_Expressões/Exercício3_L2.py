mes = {
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
    print('[ERRO] Você não escolheu um número correspondente a um mês.')