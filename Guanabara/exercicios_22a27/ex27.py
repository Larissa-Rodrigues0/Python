"""
Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida
o primeiro e o ultimo nome separadamente.

Ex: Ana Maria de Souza
primeiro = Ana
último = Souza
"""

nome = input("Escreva um nome: ").strip()

print(f"Primeiro: {nome.split()[0]}")
print(f"Último: {nome.split()[-1]}")