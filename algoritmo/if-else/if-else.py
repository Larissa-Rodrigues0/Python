'''
IF-ELSE é uma estrutura condicional para tomada de decisões

OPERADORES RELACIONAIS 

IGUAL
== ( 1 == 1 TRUE) | ( 2 == 1 FALSE)

DIFERENTE
!= ( 1 != 1 FALSE) | (2 != 1 TRUE)

MENOS QUE 
< ( 1 < 1 FALSE) | ( 2 < 1 FALSE ) 

MAIOR QUE 
> ( 1 > 1 FALSE) | ( 2 > 1 TRUE)

MENOR OU IGUAL 
<= ( 1 <= 1 TRUE) | ( 2 <= 1 FALSE)

MAIOR OU IGUAL
>= ( 1 >= 1 TRUE) | ( 2 >= 1 TRUE)
 
'''

produto = input('Digite o produto: ')
quantidade = int(input('Digite a quantidade: '))

if quantidade > 0:
    print(f'Existe atualmente: {quantidade} do produto "{produto}" ')
else:
    print(f'{produto} atualmente sem estoque')
