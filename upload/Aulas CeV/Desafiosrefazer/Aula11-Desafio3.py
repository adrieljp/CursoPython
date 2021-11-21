#Faça um programa que jogue par ou ímpar com o computador.
#O jogo só sera interrompido quando o jogador PERDER.
#Mostrando um total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint
print("=-" * 13)
print("VAMOS JOGAR PAR OU ÍMPAR")
print("=-" * 13)
cont = 0
while True:
    computador = randint(0, 10)
    jogador = int(input("Diga um valor: "))
    total = computador + jogador
    jogadorescolha = ' '
    while jogadorescolha not in "PI":
        jogadorescolha = input("Par ou Ímpar [P/I]? ").strip().upper()[0]
    print(f"Você jogou {jogador} e o computador jogou {computador}. Total de {total} ", end='')
    print("DEU PAR." if total % 2 == 0 else "DEU ÍMPAR.")
    if jogadorescolha == "P":
        if total % 2 == 0:
            print("Jogador VENCEU!")
            cont += 1
        else:
            print("Jogador PERDEU!")
            break
    elif jogadorescolha == "I":
        if total % 2 == 1:
            print("Jogador VENCEU!")
            cont += 1
        else:
            print("Jogador PERDEU!")
            break
print(f"GAME OVER. Você venceu {cont} vezes.")