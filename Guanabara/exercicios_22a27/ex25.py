"""
Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome
"""

nome = input('Escreva um nome: ').strip()

if nome.upper().find('SILVA') != -1:
    print('O nome tem "SILVA"')
else:
    print('O nome NÃO tem "SILVA"')