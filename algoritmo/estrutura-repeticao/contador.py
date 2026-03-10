'''

o que é uma estrutura de repetição?

-> Serve para executar um bloco de código várias vezes
-> ENQUANTO UMA CONDIÇÃO FOR VERDADEIRA

'''

contador = 10

while contador >= 0:
    print(contador)
    contador -= 1
    
    
'''
tabuada do 5
'''

resultado = 0
contador = 0

while resultado <=50:
    print(f'5 x {contador} = {resultado}')
    contador += 1
    resultado = contador * 5