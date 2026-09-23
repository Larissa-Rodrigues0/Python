"""
Crie um programa que leie o nome completo de uma pessoa

- o nome com todas as letras maiusculas 
- o nome com todas as letras minusculas
- Quantas letras ao todo (sem considerar espaço)
- Quantas letras tem o primeiro nome
"""

nome = input("Digite seu nome completo: ")
print(nome.lower())
print(nome.upper())
print(len(nome.replace(" ", "")))
# ou: print(len(nome) - nome.count(' '))
print(len(nome.split()[0]))


