#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
km = float(input("Quantos KM foram rodados? "))
dias = int(input("Quantos dias foram alugados? "))
valordias = dias * 60
valorkm = km * 0.15
valortotal = valordias + valorkm
print(f"Foram rodados {dias} dias, portanto o valor pago pelos dias é R${valordias:.2f}")
print(f"Foram rodados {km:.2f} KM, portanto o valor pago pelos KM rodados é R${valorkm:.2f}")
print(f"O total a ser pago é R${valortotal:.2f}")