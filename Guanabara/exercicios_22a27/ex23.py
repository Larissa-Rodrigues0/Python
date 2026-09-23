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
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f'Milhar: {m}')
print(f'Centena: {c}')
print(f'Dezena {d}')
print(f'Unidade: {u}')