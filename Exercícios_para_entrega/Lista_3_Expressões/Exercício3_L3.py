'''Anacleto tem 1,20 m e cresce 2 cm por ano, enquanto Felisberto tem 1,15 m e cresce 3 cm por 
ano. Construa um algoritmo que calcule e imprima quantos anos serão necessários para que 
Felisberto seja maior que Anacleto.'''

a = 1.2
f = 1.15
anos = 0
while (f <= a):
    a += 0.02
    f += 0.03