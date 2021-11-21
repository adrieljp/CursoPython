#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
dias=int(input("Informe a quantidade de dias que o carro foi alugado: "))
km=float(input("Informe quantos km foram rodados com o carro: "))
valordia=dias*60
valorkm=km*0.15
total=valordia+valorkm
print("O valor a pagar será: R${:.2f}.".format(total))
print("Valor dos dias alugados: R${:.2f}".format(valordia))
print("Valor dos km rodados: R${:.2f}".format(valorkm))