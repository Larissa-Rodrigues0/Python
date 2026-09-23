"""
Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".
"""

nomeCidade = input('Escreva o nome de uma cidade: ')
nomeCidade = nomeCidade.upper()
if nomeCidade.split()[0] == 'SANTO':
    print('A cidade começa com o nome "SANTO"')
else:
    print('A cidade não começa com o nome "SANTO"')
    