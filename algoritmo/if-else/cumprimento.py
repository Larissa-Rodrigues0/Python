'''
O que seu programa deve fazer:
 
1.Pedir ao jogador quantos pontos de experiência ele tem (XP):
 
Menos de 100 → "Iniciante"
 
Entre 100 e 500 → "Intermediário"
 
Mais de 500 → "Veterano"
 
Use if/elif/else para essa classificação.
 
2. Depois, o programa deve perguntar qual ação o jogador deseja executar (usar match case):
 
"A" → Atacar
 
"D" → Defender
 
"F" → Fugir
 
Qualquer outra tecla → "Ação inválida"
 
Mostre uma mensagem apropriada para cada ação, como:
 
"Você avançou para o ataque!"
 
"Você levantou o escudo!"
 
"Você fugiu da batalha!"
        
'''
import os

print("\nolá Jogador, vamos brincar um pouco?")
xp = int(input('Quantos pontos XP seu personagem tem? '))

if xp < 100:
    print('\nSeu personagem é iniciante!\n')  
    os.system('pause')     
    
elif xp < 500:
    print('\nSeu personagem é intermediario\n')
    os.system('pause')     
    
else:
    print('\nSeu personagem é Veterano\n')
    os.system('pause')     
    
    
print('''\n == Ações: == \n
    "A" → Atacar
 
    "D" → Defender
 
    "F" → Fugir
      ''')
acao = input('Qual ação você quer que seu personagem faça?')

if acao == acao.lower():
    acao = acao.upper()

match acao:
    case 'A':
        print('- Você avançou para o ataque!\n')
        os.system('pause') 
            
    case 'D':
        print('- Você levantou o escudo!\n')
        os.system('pause')     
        
    case 'F':
        print('- Você fugiu da batalha!\n')
        os.system('pause') 
    
    case _:
        print('Parece que você escolheu uma opcão inválida, volte e tente novamente!\n')   
        os.system('pause') 
        
print('\nParabens! Você conclui sua ação com exito!')