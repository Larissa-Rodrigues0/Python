# Crie um programa que leia um numero real qualquer pelo teclado e mostre na tela a sua porção inteira.
# Digite um numero: 6.232354 
# O numero 6.232354 tem a parte inteira 6

import math
numQuebrado = float(input('Escreva um numero real: '))
# numInteiro = math.trunc(numQuebrado)
# ou: numInteiro = int(numQuebrado)
print(f'O numero {numQuebrado} tem a parte inteira {math.trunc(numQuebrado)}')