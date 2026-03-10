import os
from funcoes import *

os.system('cls')
print('\n ------------------------ ')
print('   🎲 BANCO DE DADOS 🎲    ')
print(' ------------------------ \n')
  
while True:    
        
    conta_usuario = cadastro_usuario()

    if conta_usuario != 'cpf-invalido':
        os.system('cls')
        print('Usuario cadastrado com sucesso! \n')
        os.system('pause')
            
        while True:
            menu_opcoes()
            op = input('Escolha sua opção: ')
            
            match op:
                case '1': depositar(conta_usuario)
                case '2': sacar(conta_usuario)
                case '3': verificar_saldo(conta_usuario)
                case '4': verificar_extrato(conta_usuario)
                case '5':
                    os.system('cls')
                    print('Você escolheu sair!')
                    print('Obrigada por testar nosso sistema!\n')
                    os.system('pause')
                    break
        break
                
'''        continuar = input('Deseja realizar outra operação? (S = sim | N = não)').upper()
        if continuar == 'S' or 'SIM':
            continue
        else:
            print('Obrigada por testar nosso sistema!')
            os.system('pause')
            break'''