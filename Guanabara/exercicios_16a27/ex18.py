# Faça um programa que leia um angulo qualquer 
# e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
#import math
from math import radians, sin, cos, tan

print('Informe:\n')
angulo = float(input('Valor do ângulo: '))

angulo = radians(angulo)

seno = sin(angulo)
cosseno = cos(angulo)
tangente = tan(angulo)

print('\n~ Valores do ângulo ~ ')
print(f'Seno: {seno:.2f}\nCosseno: {cosseno:.2f}\nTangente: {tangente:.2f}')