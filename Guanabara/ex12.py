# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

p = float(input('Digite o preço do produto: R$ '))
novo_preco = p - (p * 0.05)
print(f'O novo preço do produto com 5% de desconto é R$ {novo_preco:.2f}')