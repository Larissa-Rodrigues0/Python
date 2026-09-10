# Escreva um programa que pergunte a quantidade de KM percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0.15 por KM rodado.

print("\nInformações necessarias:")
quantKM = float(input("Quantidade de KM percorrido: "))
quantDias = int(input("Quantidade de dias alugados: "))
# pagarTotal = (quantKM * 0.15) + (quantDias * 60)
pagarKM = quantKM * 0.15
pagarDias = quantDias * 60
pagarTotal = pagarDias + pagarKM
print(f"\n- Valor a pagar KM: {pagarKM}\n- Valor a pagar dia: {pagarDias}\n- Valor total a pagar: {pagarTotal}")