'''Escrever um programa para determinar quantas pessoas acima de 18 anos têm uma estatura 
superior a 1,60 metros. O usuário deverá informar a idade e o altura de cada pessoa. O programa 
deve terminar quando o usuário informar um valor negativo para a idade. '''

n = 0
while True:
    idade = int(input(f'Digite a idade: '))
    if (idade < 0):
        break
    altura = float(input('Digite a altura: '))
    if (idade >= 18) and (altura > 1.60):
        n += 1        
print(f'Ao total são com {n} pessoas acima de 18 anos com mais de 1.60 metros de altura.')        