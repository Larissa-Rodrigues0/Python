notas = [8, 5, 9, 6, 7]
contarAprovados = 0
contarAcompanhados = 0
 
for nota in notas:
    if nota >= 7:
        print(f"O fúncionario está aprovado")
        contarAprovados = contarAprovados + 1
    else:
        print(f"O fúncionario está em acompanhamento")
        contarAcompanhados = contarAcompanhados + 1
 
print(f"Quantidades de fúncionarios aprovados: {contarAprovados}")
print(f"Quantidades de fúncionarios em acompanhamento: {contarAcompanhados}")
 