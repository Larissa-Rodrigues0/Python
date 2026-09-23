"""
Faça um programa que leie um número de 0 a 9999 e mostre na tela 
cada um dos digitos separados

Ex: Digite um numero: 1235
unidade: 5
dezena: 3
centena: 2
milhar: 1
"""

num = input('Escreva um numero de 0 a 9999: ')
print(f'Milhar: {num[:1]}')
print(f'Centena: {num[1:2]}')
print(f'Dezena {num[2:3]}')
print(f'Unidade: {num[3:4]}')