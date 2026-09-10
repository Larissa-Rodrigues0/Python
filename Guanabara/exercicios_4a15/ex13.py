# Faça um algoritmo que leia o salario de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Digite o salário do funcionário: R$ '))
novo_salario = salario + (salario * 0.15)
print(f'O novo salário do funcionário com 15% de aumento é R$ {novo_salario:.2f}')