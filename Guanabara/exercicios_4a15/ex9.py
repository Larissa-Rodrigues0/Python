# # Faça um programa que leia um numero inteiro qualquer e mostre na tela a sua tabuada.

n = int(input('Digite um número inteiro: '))

for i in range(1, 11):
    print(f'{n} x {i} = {n * i}')