import os

def cadastro_usuario():
    nome = input('Digite o seu nome completo: ')
    cpf = input('Digite o seu CPF (APENAS NÚMEROS): ')
    nascimento = input('Digite a sua data de nascimento (DDD/MM/AA): ')
    
    if len(cpf) != 11:
        print('\nO seu CPF está incorreto!\nRetorne e tente novamente.\n')
        return 'cpf-invalido'
    else:
        conta = {
            "nome": nome,
            "cpf": cpf,
            "data_nascimento": nascimento,
            "saldo": 0,
            "historico": []
        }
        return conta
      
def menu_opcoes():
    os.system('cls')
    print(''' 
    == Menu Opções ==
    1. Depositar
    2. Sacar
    3. Verificar saldo
    4. Verificar extrato
    5. Sair
          ''')      
  
def depositar(conta):
    os.system('cls')
    print('Você escolheu Depositar!!')
    
    valor = input("Digite o valor a depositar: R$ ")
    
    if not valor.isdigit():
        print('\nValor inválido! Digite apenas números inteiros')
        os.system('pause')
        return
    
    valor_int = int(valor)
    
    if valor_int <= 0:
        print('\nValor do depósito deve ser maior que R$ 0')
        os.system('pause')
        return
    
    conta["saldo"] += valor_int
    conta["historico"].append(f'Depósito R$ {valor_int}')
    print('\nDepósito realizado com sucesso!!')     
    os.system('pause')
        
def sacar(conta):
    os.system('cls')
    print('Você escolheu Saque!!')
    valor = input("Digite o valor do saque: R$ ")
    
    if not valor.isdigit():
        print('\nValor inválido! Digite apenas números inteiros')
        os.system('pause')
        return
    
    valor_int = int(valor)
    
    if valor_int <= 0 or valor_int > conta["saldo"]:
        print('\nDigite um valor válido!')
        os.system('pause')
        return
    
    conta["saldo"] -= valor_int
    conta["historico"].append(f'Saque R$ {valor_int}')
    print('\nSaque realizado com sucesso!!')
    os.system('pause')
         
def verificar_saldo(conta):
    os.system('cls')
    print('Você escolheu Verificar Saldo!')
    print(f'Saldo atual R$ {conta["saldo"]}\n')
    os.system('pause')
    
def verificar_extrato(conta):
    os.system('cls')
    print('Você escolheu Verificar Extrato!')
    if len(conta["historico"]) <= 0:
        print('Nenhum movimento registrado!')
        os.system('pause')
        return 
    else:
        print('Extrato atual:\n')
        for registro in conta["historico"]:
            print(registro)
        print('\n')
        os.system('pause')
        return
    
    
