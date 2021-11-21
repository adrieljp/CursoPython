#Crie um programa que faça o computador jogar Jokenpô com você
from random import randint
from time import sleep
itens = ("Pedra", "Papel", "Tesoura")
computador = randint(0, 2)
jogador = int(input('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA
Qual sua jogada? '''))
print("JO ", end='', flush=True), sleep(0.85), print("KEN ", end='', flush=True), sleep(0.85), print("PO\n", end='', flush=True), sleep(0.85)
print("-=-" * 15)
print("Computador jogou {}.".format(itens[computador]))
print("Jogador jogou {}.".format(itens[jogador]))
print("-=-" * 15)
if computador == 0:
    if jogador == 1:
        print("JOGADOR VENCEU.")
    elif jogador == 2:
        print("JOGADOR PERDEU.")
    elif jogador == 0:
        print("EMPATE.")
    else:
        print("JOGADA INVÁLIDA.")
elif computador == 1:
    if jogador == 2:
        print("JOGADOR VENCEU.")
    elif jogador == 0:
        print("JOGADOR PERDEU.")
    elif jogador == 1:
        print("EMPATE.")
    else:
        print("JOGADA INVÁLIDA.")
elif computador == 2:
    if jogador == 0:
        print("JOGADOR VENCEU.")
    elif jogador == 1:
        print("JOGADOR PERDEU.")
    elif jogador == 2:
        print("EMPATE.")
    else:
        print("JOGADA INVÁLIDA.")