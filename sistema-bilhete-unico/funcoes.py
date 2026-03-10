import os

def cadastro_usuario():
    nome = input('Digite seu nome: ')
    cpf = input('Digite seu cpf: ')
    
    if len(cpf) != 11:
        print('\nO seu CPF está incorreto!\nRetorne e tente novamente.\n')
        return 'cpf-invalido'
    else:
        bilhete = {
           "nome": "Fulano",
            "cpf": "12345678900",
            "saldo": 0.0,
            "extrato": []
            }
        return bilhete
    
def menu_opcoes():
    os.system('cls')
    print(''' 
    == Menu Opções ==
    1 - Recarregar bilhete
    2 - Passar na catraca
    3 - Ver saldo
    4 - Ver extrato
    5 - Encerrar sistema
          ''')   
    
def recarregar(bilhete):
    os.system('cls')
    print('Você escolheu Recarregar!!')
    
    valorRecarga = input('Qual o valor da recarga: ')
    
    if not valorRecarga.isdigit():
        print('\nValor inválido! Digite apenas números inteiros')
        os.system('pause')
        return
    
    valor_int = int(valorRecarga)
    return valor_int
    
def validar_valor(bilhete, valor):
    if valor <= 0:
        print('\nValor da recarga deve ser maior que R$ 0')
        os.system('pause')
        return
    
    bilhete["saldo"] += valor
    bilhete["extrato"].append(f'Recarga: R$ {valor}')
    print('\nRecarga realizada com sucesso!!')   
    print(f'Saldo atual R$ {bilhete["saldo"]}\n')  
    os.system('pause')
    
def passar_catraca(bilhete):
    os.system('cls')
    
    if bilhete["saldo"] >= 4.40:
        bilhete["saldo"] -= 4.40
        
        bilhete["extrato"].append(f'Passagem: R$ -4.40')
        print('\nPassagem liberada!')   
        os.system('pause')
    else:
        bilhete["extrato"].append(f'Tentativa sem saldo!')
        print('\nSaldo insuficiente!')   
        os.system('pause')
     
def ver_saldo(bilhete):
    os.system('cls')
    print('Você escolheu ver Saldo!')
    print(f'Saldo atual R$ {bilhete["saldo"]}\n')
    os.system('pause')
    
def mostrar_extrato(bilhete):
    os.system('cls')
    print('Você escolheu ver Extrato!')
    if len(bilhete["extrato"]) <= 0:
        print('Nenhum movimento registrado!')
        os.system('pause')
        return 
    else:
        print('Extrato atual:\n')
        for registro in bilhete["extrato"]:
            print(registro)
        print('\n')
        os.system('pause')
        return