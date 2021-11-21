# Desenvolva um programa que pergunta a distância de uma viagem em KM. Cacule o preço da passagem, cobrando R$0.50 por KM para viagens de até 200KM
# E R$0.45 para viagens mais longas.
from time import sleep
km = float(input("Informe a distância da viagem em KM: "))
print(f"A distância da sua viagem é {km:.2f}")
print(f"CALCULANDO PREÇO...")
sleep(1)
if km <= 200:
    viagem = km * 0.50
    print(f"O preço da sua viagem sairá por R${viagem:.2f}")
else:
    viagem = km * 0.45
    print(f"O preço da sua viagem sairá por R${viagem:.2f}")