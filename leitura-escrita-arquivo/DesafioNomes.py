'''
O que você deve fazer
Ler o arquivo nomes_ficticios.txt
Converter todos os nomes para minúsculo
Criar uma nova lista com os nomes convertidos
Salvar o resultado em um novo arquivo chamado:

nomes_tratados.txt

Após converter todos os nomes para minúsculo:
Ordene a lista em ordem alfabética
Salve o resultado já ordenado no arquivo final

'''

 
with open('nomes_ficticios.txt', 'r', encoding='utf-8') as ArquivoNome:
    nomes = ArquivoNome.readlines()
        
nomes_ordenados = sorted(nomes)

with open('nomes.txt', 'w', encoding='utf-8') as ArquivoOrdem:
    ArquivoOrdem.writelines(nomes_ordenados)
    
with open('nomes.txt', 'r', encoding='utf-8') as ArquivoNome:
    nomes = ArquivoNome.readlines()
        
with open('nomes_tratados.txt', 'w', encoding='utf-8') as arquivoSaida:
    for nome in nomes:
        arquivoSaida.write(nome.lower())
        
        
        
    
    