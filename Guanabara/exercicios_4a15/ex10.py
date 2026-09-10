# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. 
# Considere US$1,00 = R$3,27

dinheiro = float(input('Digite quanto dinheiro você tem na carteira: R$ '))
dolar = dinheiro / 3.27
print(f'Com R${dinheiro:.2f} você pode comprar US${dolar:.2f}')