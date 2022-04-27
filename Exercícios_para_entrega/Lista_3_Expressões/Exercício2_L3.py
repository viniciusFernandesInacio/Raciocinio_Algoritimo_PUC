'''Elabore um programa que calcule e apresente os 6 primeiros termos da progressão aritmética 
(PA) abaixo, sendo o primeiro termo a1 =  1 e razão  r=3. Faça o TESTE DE MESA. '''

primeiro = 1
razao = 3
n = 6

ultimo = primeiro + (n-1)*razao
ultimo = ultimo + 1

for c in range(primeiro, ultimo, razao):
    print(c)