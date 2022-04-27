import sys


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
    sys.exit(0)