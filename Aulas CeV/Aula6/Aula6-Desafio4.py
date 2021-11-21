# Desenvolva um programa que pergunta a distância de uma viagem em KM. Cacule o preço da passagem, cobrando R$0.50 por KM para viagens de até 200KM
# E R$0.45 para viagens mais longas.

dis=float(input("Digite a distância da sua viagem em KM: "))
ate200km=dis * 0.50
mais200km=dis * 0.45
if dis <= 200:
    print("Você irá pagar R${:.2f} pela sua viagem.".format(ate200km))
else:
    print("Você irá pagar R${:.2f} pela sua viagem.".format(mais200km))