"""
Faça um programa que leia uma frase pelo teclado e mostre:

- Quantas vezes aparece a letra "A"
- Em que posição ela aparece a primeira vez
- Em que posição ela aparece pela ultima vez
"""

frase = input('Escreva uma frase: ').strip().lower()

print(f'A letra "A" aparece {frase.count("a")} vezes na frase.')

print(f'A primeira letra "A" apareceu na posição {frase.find("a") + 1}')

print(f'A última letra "A" apareceu na posição {frase.rfind("a") + 1}')