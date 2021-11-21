# Escreva um programa que leia a velocidade de um carro, se ele ultrapassar 80KM/H mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7.00 por cada KM acima do limite.
velocidade=float(input("Digite a velocidade em KM/H: "))
multa=(velocidade-80)*7
if velocidade > 80:
    print("A sua velocidade ultrapassa o limite e será aplicada uma multa de R${:.2f}.".format(multa))
else:
    print("Você está dirigindo na velocidade permitida.")
print("Obrigado. Dirija com segurança!")