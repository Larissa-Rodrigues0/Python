# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from time import sleep
from random import choice

alunos = []
quantAlunos = 4

for i in range(quantAlunos):
    nome = input(f'Nome do {i+1}° aluno: ')
    alunos.append(nome)

print('\nEscolhendo ordem das apresentações...')
sleep(2)

# pode ser usado shuffle tbm
for i in range(len(alunos)):
    sorteado = choice(alunos)
    print(f'{i+1}° apresentação: {sorteado}')
    alunos.remove(sorteado)

