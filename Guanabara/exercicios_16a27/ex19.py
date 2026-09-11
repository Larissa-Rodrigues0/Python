# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome escolhido.

from time import sleep
from random import choice

alunos = []

for i in range(4):
    nome = input(f'Nome do {i+1} aluno: ')
    alunos.append(nome)

print("\nLista de Alunos:")
for aluno in alunos:
    print(aluno)

print('\nEscolhendo um aluno...')
sleep(2)

sorteado = choice(alunos)
print(f'O sorteado foi: {sorteado}')