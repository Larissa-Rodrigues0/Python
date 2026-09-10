# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente 
# de um triangulo retângulo, calcule e mostre o comprimento da hipotenusa.

import math 

print('Informe: \n')
cateto_oposto = float(input('Cateto oposto: '))
cateto_adjacente = float(input('Cateto adjacente: '))

hipotenusa = math.hypot(cateto_oposto, cateto_adjacente)
print(f'A hipotenusa desse tringulo é: {hipotenusa}')