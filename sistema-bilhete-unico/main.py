'''
Cenário
A empresa  TransParaty quer um sistema simples para simular um Bilhete Único.
O usuário cria seu bilhete e consegue recarregar, passar na catraca, 
ver saldo e ver histórico de uso (extrato).

--Regras do sistema
Tarifa fixa: R$ 4,40 por passagem
O bilhete começa com saldo 0
Se não tiver saldo suficiente para a tarifa, bloqueia a passagem
O sistema deve registrar no “extrato” as ações (recarregou, passou na catraca, tentativa sem saldo)


'''
import os
from funcoes import *

os.system('cls')
print('\n ------------------------ ')
print('  📓  BILHETE ÚNICO 📓    ')
print(' ------------------------ \n')
  
while True:    
        
    conta_usuario = cadastro_usuario()

    if conta_usuario != 'cpf-invalido':
        os.system('cls')
        print('Bilhete cadastrado com sucesso! \n')
        os.system('pause')
            
        while True:
            menu_opcoes()
            op = input('Escolha sua opção: ')
            
            match op:
                case '1': 
                    valor = recarregar(conta_usuario)
                    validar_valor(conta_usuario,valor)
                case '2': passar_catraca(conta_usuario)
                case '3': ver_saldo(conta_usuario)
                case '4': mostrar_extrato(conta_usuario)
                case '5':
                    os.system('cls')
                    print('Você escolheu sair!')
                    print('Obrigada por testar nosso sistema!\n')
                    os.system('pause')
                    break
        break
                
