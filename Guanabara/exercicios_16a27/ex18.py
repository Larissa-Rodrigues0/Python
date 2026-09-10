# Faça um programa que leia um angulo qualquer 
# e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math

print('Informe:\n')
angulo = float(input('Valor do ângulo: '))

angulo = math.radians(angulo)

seno = math.sin(angulo)
cosseno = math.cos(angulo)
tangente = math.tan(angulo)

print('\n~ Valores do ângulo ~ ')
print(f'Seno: {seno:.2f}\nCosseno: {cosseno:.2f}\nTangente: {tangente:.2f}')