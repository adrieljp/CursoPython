# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5.
# E peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.
# Usar a biblioteca library e o comando randint
from random import randint
while True:
    computador = randint(0, 5)
    print("-=-" * 17)
    print("Pensei em um número entre 0 e 5, tente adivinhar!")
    print("-=-" * 17)
    while True:
        user = int(input("Seu palpite: "))
        if user >= 0 and user <= 5:
            if user == computador:
                print("\nAH NÃO! Você ganhou de mim.")
                print(f"Eu pensei no número {computador}.")
                break
            else:
                print("\nHAHAHA! Eu ganhei de você.")
                print(f"Eu pensei no número {computador}.")
                break
    op = ' '
    while op not in "SN":
        op = input("\nGostaria de jogar novamente [S/N]? ").strip().upper()[0]
    if op == "S":
        continue
    else:
        break