import os
 
def menu():
    print('''
          Menu de Opções:
          1. Somar
          2. Subtrair
          3. Multiplicar
          4. Dividir
          5. Porcentagem
          ''')
 
def somar(n1,n2):
    return n1 + n2
 
def subtrair(n1,n2):
    return n1 - n2
 
def multiplicar(n1,n2):
    return n1 * n2
 
def dividir(n1,n2):
    return n1 / n2
 
def porcetagem(valor, percentual):
    return (valor * (percentual/100))
 
def valores():
    n1 = float(input('Qual o primeiro número desejado? '))
    n2 = float(input('Qual o segundo número desejado? '))  
    return n1, n2
 
#-------------------------------------------------------------------------------------
 
print('\nBem Vindo a Calculadora! \nVamos começar?')

while True:
    menu()
    op = int(input('Qual é a sua opção?\nPor Favor, digite o número da escolha:\n = '))
    
    os.system('cls')
    match op:
        case 1:
            print('\nVocê escolheu somar!')
            n1, n2 = valores()
            print(f'O resultado do seu calculo é: {somar(n1,n2)}\n')
            os.system('pause')
        
        case 2:
            print('\nVocê escolheu subtrair!')
            n1, n2 = valores()
            print(f'O resultado do seu calculo é: {subtrair(n1,n2)}\n')
            os.system('pause')
        
        case 3:
            print('\nVocê escolheu multiplicar!')
            n1, n2 = valores()
            print(f'O resultado do seu calculo é: {multiplicar(n1,n2)}\n')
            os.system('pause')
        
        case 4:
            print('\nVocê escolheu dividir!')
            n1, n2 = valores()
            if n2 == 0:
                print('Divisão por 0 não é permitido!')
            else:
                print(f'O resultado do seu calculo é: {dividir(n1,n2)}\n')
                os.system('pause')
        
        case 5:
            print('\nVocê escolheu a Porcentagem!')
        
            n1 = float(input('Qual o valor para fazer a porcentagem?'))
            n2 = float(input('Qual o valor da porcentagem?'))
        
            print(f'O resultado do seu calculo é: {porcetagem(n1,n2)}\n')
            os.system('pause')
        
        case _:
            print('\nVocê escolheu um número invalido!\nVoltando ao inicio...')
            os.system('pause')
            continue
    
    continuar = input('\nDeseja fazer outro calculo?\nS = Sim | N = Não\n =').upper()
    if continuar == 'S':
        os.system('cls')
        continue
    else:
        print('\nVocê escolheu sair!\nObrigada por utilizar nossa calculadora!\n')
        os.system('pause')
        break
