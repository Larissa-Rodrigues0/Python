import os

while True:
    print('\nVamos fazer uma tabuada?')
    numeroTabuada = int(input('Escolha um numero para a tabuada: '))
    if numeroTabuada < 0:
        print("\nNúmero negativo não é permitido, por favor insira um número positivo!")
        continue
    else:
        numeroLimite = int(input('\nQual o número limite?\n(Até qual numero quer que o calculo forneça): '))
 
        resultado = 0
        contador = 0
 
        while resultado <= (numeroLimite * numeroTabuada):
            print(f'{numeroTabuada} x {contador} = {resultado}')
            contador += 1
            resultado = contador * numeroTabuada
           
        print(f'\nEsse foi o resultado para a tabuada do número {numeroTabuada}!')
       
    resposta = input('Deseja fazer outra tabuada? \nS = Sim | N = Não: ').upper()
    if resposta == "S":
        continue
    else:
        print('\nObrigada por participar!')
        os.system('pause')
        break