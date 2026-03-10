import os

print(' == Criador de Pastas Automáticos == ')
print('LOGIN:')
usuario = input('Nome do Usuario: ')
senha = input('Senha: ')

if usuario == 'cliente123' and senha == 'cliente123':
    
    while(True):

        print("Qual o nome da pasta que deseja criar?")
        nomePasta = input("= ")
        if nomePasta == "":
            print('O nome da pasta não pode ser vazio!\n')
            continue
        
        nomePasta = nomePasta.lower()
       
        if not os.path.exists(nomePasta):
            os.makedirs(nomePasta)
            print(f"\nPasta '{nomePasta}' criada.")
        else:
            print(f"\nPasta '{nomePasta}' já existe.")
            
        print("Deseja voltar para criar novamente? S = sim | N = não")
        confirmacao = input('= ').upper()
        if confirmacao == 'S':
            continue
        else:
            print('Obrigada por usar nosso sistema!')
            os.system('pause')
            break
        
else:
    print('Nome de usuario ou senha errado!')
