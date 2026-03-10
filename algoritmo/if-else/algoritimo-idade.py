'''
Dona Maria precisa de um algoritmo que faça a seguinte decisão:

1. Se a idade for menor que 12, deve mostrar a mensagem "criança"
2. Se a idade for menor que 18, deve mostrar a mensagem "adolescente"
3. Se a idade for menor que 60, deve mostrar a mensagem "adulto"
4. Se a idade não for nenhuma dessas opções, deve mostrar "idoso"

'''

print(" == Sistema da Dona Maria == ")
idade = int(input('Qual a idade escolhida? '))

if idade < 12:
    print(f"A idade colocada foi: {idade}\nPortanto a pessoa é uma criança")
elif idade < 18:
    print(f"A idade colocada foi: {idade}\nPortanto a pessoa é uma adolescente")
elif idade < 60:
    print(f"A idade colocada foi: {idade}\nPortanto a pessoa é uma adulto")
else:
    print(f"A idade colocada foi: {idade}\nPortanto a pessoa é uma idoso")
