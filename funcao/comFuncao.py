def menu():
    print('''
    Menu de Opções:
    1. Cadastrar Aluno
    2. Listar Alunos
    3. Mostrar o total de alunos cadastrados
    4. Sair
          ''')

def cadastroAluno():
    print('\nVocê escolheu cadastrar Aluno!\n')
    nomeAluno = input('Digite o nome do Aluno: ')
    nota1 = int(input('Digite a primeira nota dele: '))
    nota2 = int(input('Digite a segunda nota dele: '))
            
    if (nota1 + nota2) / 2 >= 7:
    #alunos.append(nomeAluno,'= Aprovado' )
        situacao = 'Aprovado'
    else:
        situacao = 'Reprovado'
                
    alunos.append(f'{nomeAluno} - {situacao}')
    print('\nAluno Cadastrado com sucesso!')
    os.system('pause')
    os.system('cls')

def listarAluno():
    if len(alunos) > 0:
        for aluno in alunos:
            print(aluno)
    else:
        print('A lista de Alunos está vazia!')
    os.system('pause')
    os.system('cls')
    
def totalAluno():
    if len(alunos) != 0:
        print(f'Total de alunos cadastrados: {len(alunos)}')
        os.system('pause')
    else:
        print('Nenhum aluno cadastrado ainda.')
        os.system('pause')
#------------------------------------------------------------------

import os
alunos = []

print('\n === SISTEMA ESCOLAR === ')
while True:
    menu()
    op = int(input('Qual sua opção desejada?\n= '))
    if op == 4:
        print('Saindo do sistema...')
        break
    
    match op:
        case 1: cadastroAluno()
                
        case 2: listarAluno()
        
        case 3: totalAluno()
        
        case _:
            print('Opção Invalida!')
            continue
        