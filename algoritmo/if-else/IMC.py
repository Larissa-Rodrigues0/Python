<<<<<<< HEAD
'''
Criar uma estrutura de decisão (if, elif, else) que classifique o IMC (Índice de Massa Corporal) com base no valor digitado pelo usuário.
 
Enunciado:
 
Você foi contratado por uma academia para desenvolver um programa que ajude os alunos a classificarem seu IMC com base no valor informado.

Seu desafio é receber o valor do IMC pelo usuário e imprimir a classificação correta:
 
Faixa de IMC	  Classificação
Abaixo de 18.5	 Abaixo do peso
De 18.5 até 24.9    Peso normal
De 25 até 29.9	  Sobrepeso
De 30 até 39.9	  Obesidade
Acima de 40	     Obesidade grave
 
Critérios para o desafio estar completo:
O código deve utilizar input() para receber o valor do IMC.
Deve conter uma estrutura if, elif, else.
Deve imprimir a classificação correta conforme a tabela.
Enviar o link do repositório com o Código
'''
print(" == Sistema para calcular IMC == \nIndique sua altura e peso: ")
altura = float(input("Altura: "))
peso = float(input("Peso: "))

resul = (peso/(altura*altura))

if resul > 18.5:
    print(f"O resultado do calculo foi {resul}\nPortanto sua classificação é abaixo do peso")
elif resul > 24.9:
    print(f"O resultado do calculo foi {resul}\nPortanto sua classificação é peso normal")
elif resul > 29.9:
    print(f"O resultado do calculo foi {resul}\nPortanto sua classificação é Sobrepeso")
elif resul > 39.9:
    print(f"O resultado do calculo foi {resul}\nPortanto sua classificação é Obesidade")
else:
    print(f"O resultado do calculo foi {resul}\nPortanto sua classificação é Obesidade Grave")
=======
print(" == Sistema para calcular IMC == \nIndique sua altura e peso: ")
altura = float(input("Altura(m): "))
peso = float(input("Peso(kg): "))
 
resul = peso/(altura*altura)
 
if resul < 18.5:
    print(f"O resultado do calculo foi {resul:.2f}\nPortanto sua classificação é abaixo do peso")
elif resul < 24.9:
    print(f"O resultado do calculo foi {resul:.2f}\nPortanto sua classificação é peso normal")
elif resul < 29.9:
    print(f"O resultado do calculo foi {resul:.2f}\nPortanto sua classificação é Sobrepeso")
elif resul < 39.9:
    print(f"O resultado do calculo foi {resul:.2f}\nPortanto sua classificação é Obesidade")
else:
    print(f"O resultado do calculo foi {resul:.2f}\nPortanto sua classificação é Obesidade Grave")
 

 
>>>>>>> 32dd66539fa32b7220539f10f301b663522c33fe
