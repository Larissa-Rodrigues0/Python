#Montar um sistema de cadastro de alunos e notas

'''
Menu opções:
1. Cadastrar Aluno
2. Listar a alunos
3. Sair
'''

#Lista alunos
import os
alunos = []

print('\n === SISTEMA ESCOLAR === ')
while True:
    print('''
    Menu de Opções:
    1. Cadastrar Aluno
    2. Listar Alunos
    3. Sair
          ''')
    op = int(input('Qual sua opção desejada?\n= '))
    if op == 3:
        print('Saindo do sistema...')
        break
    
    match op:
        case 1:
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
                
        case 2:
            for aluno in alunos:
                print(aluno)
            os.system('pause')
            os.system('cls')
        
        case _:
            print('Opção Invalida!')
            continue
            