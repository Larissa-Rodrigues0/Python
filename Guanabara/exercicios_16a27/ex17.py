# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente 
# de um triangulo retângulo, calcule e mostre o comprimento da hipotenusa.

#import math 
from math import hypot

print('Informe o comprimento: \n')
cOposto = float(input('Cateto oposto: '))
cAdjacente = float(input('Cateto adjacente: '))

hipotenusa = hypot(cOposto, cAdjacente)
print(f'A hipotenusa desse tringulo é: {hipotenusa}')