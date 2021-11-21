# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5.
# E peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.
# Usar a biblioteca library e o comando randint

from random import randint
from time import sleep
print("-=-" * 20)
print("Eu irei pensar em um número de 0 a 5. Tente adivinhar!")
print("-=-" * 20)
computador = randint(0, 5)
jogador = int(input("Qual número você acha que é? "))
print("PROCESSANDO...")
sleep(2)
if jogador == computador:
    print("Parabéns, você adivinhou o número e ganhou a rodada!")
else:
    print("PERDEU! Eu pensei no número {} e não no {}.".format(computador, jogador))