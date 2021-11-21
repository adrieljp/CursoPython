# Escreva um programa que leia a velocidade de um carro, se ele ultrapassar 80KM/H mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7.00 por cada KM acima do limite.
velocidade = float(input("Velocidade: "))
kmacima = velocidade - 80
multa = kmacima * 7
print("A velocidade permitida é 80KM/H")
if velocidade > 80:
    print(f"Você ultrapassou o limite de velocidade em {kmacima:.2f}KM/H")
    print(f"Sua multa é de R${multa:.2f}")
else:
    print("Você está no limite de velocidade.")
print("Dirija com segurança!")