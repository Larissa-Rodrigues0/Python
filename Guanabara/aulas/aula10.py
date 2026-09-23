# condiçoes simples e compostas

nome = str(input('Qual é seu nome? '))
if nome == 'Lari':
    print('Que nome bonito você tem')
else:
    print('Seu nome é tão normal')
print(f'Tenha um otimo dia {nome}')

###################################
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1+n2) / 2
print(f'A sua media foi: {m:.1f}')
print(f'Parabéns' if m>=6 else 'Estude mais')