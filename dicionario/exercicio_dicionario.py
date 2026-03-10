produto = {
    "nome": "",
    "preço": "",
    "quantidade em estoque": "",
    "categoria:": ""
}

print('== CRIANDO UM PRODUTO ==\n')

produto["nome"] = input("Qual o nome do produto para ser adicionado?")
produto["preço"] = input("Qual o preço do produto para ser adicionado?")
produto["quantidade em estoque"] = input("Qual a quantidade em estoque do produto para ser adicionado?")
produto["categoria"] = input("Qual a categoria do produto para ser adicionado?")


print("\nProduto cadastrado:")
print("Todas as informações do produto: ")
print(f' Nome: {produto["nome"]} \n Preço: R${produto["preço"]} \n Quantidade em estoque: R${produto["quantidade em estoque"]} \n Categoria: R${produto["categoria"]}')
print('\nApenas informações basicas:')
print(f'Nome: {produto["nome"]} | Preço: R${produto["preço"]}')


# ------------------------------------------


print('\nDesafio Extra')

produtos = [
    {"nome": "Mouse", "preco": 150},
    {"nome": "Teclado", "preco": 200},
    {"nome": "Monitor", "preco": 1200}
]

for item in produtos:
    print(f'Nome: {item["nome"]} | Preço: R${item["preco"]}')