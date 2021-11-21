#Crie um programa que faça o computador jogar Jokenpô com você
from random import randint
from time import sleep
from os import system
contpartidas = contjogadorvitorias = contcomputadorvitorias = contempates = 0
while True:
    print("-=" * 10)
    print("      JOKENPÔ")
    print("-=" * 10)   
    op = int(input("[ 1 ]NOVO JOGO\n[ 2 ]ESTATÍSTICAS\n[ 3 ]SAIR DO JOGO\nSua escolha: "))
    system('cls')
    if op == 1:
        while True:
            print("-=-" * 7)
            print("Vamos jogar JOKENPÔ!")
            print("-=-" * 7)
            computador = randint(1, 3)
            jogador = int(input("Suas opções\n[ 1 ]PEDRA\n[ 2 ]PAPEL\n[ 3 ]TESOURA\n[ 0 ]Voltar pro menu principal\nQual sua jogada? "))
            system('cls')
            if jogador == 0:
                break
            elif jogador == 1:
                print("-=-" * 10)
                print("Jogador jogou Pedra")
                contpartidas += 1
                if computador == 1:
                    print("Computador jogou Pedra")
                    print("EMPATE!")
                    print("-=-" * 10)
                    contempates += 1
                    sleep(1)
                elif computador == 2:
                    print("Computador jogou Papel")
                    print("Jogador PERDEU!")
                    print("-=-" * 10)
                    contcomputadorvitorias += 1
                    sleep(1)
                else:
                    print("Computador jogou Tesoura")
                    print("Jogador VENCEU!")
                    print("-=-" * 10)
                    contjogadorvitorias += 1
                    sleep(1)
            elif jogador == 2:
                print("-=-" * 10)
                print("Jogador jogou Papel")
                contpartidas += 1
                if computador == 1:
                    print("Computador jogou Pedra")
                    print("Jogador VENCEU!")
                    print("-=-" * 10)
                    contjogadorvitorias += 1
                    sleep(1)
                elif computador == 2:
                    print("Computador jogou Papel")
                    print("EMPATE")
                    print("-=-" * 10)
                    contempates += 1
                    sleep(1)
                else:
                    print("Computador jogou Tesoura")
                    print("Jogador PERDEU!")
                    print("-=-" * 10)
                    contcomputadorvitorias += 1
                    sleep(1)
            elif jogador == 3:
                print("-=-" * 10)
                print("Jogador jogou Tesoura")
                contpartidas += 1
                if computador == 1:
                    print("Computador jogou Pedra")
                    print("Jogador PERDEU!")
                    print("-=-" * 10)
                    contcomputadorvitorias += 1
                    sleep(1)
                elif computador == 2:
                    print("Computador jogou Papel")
                    print("Jogador VENCEU!")
                    print("-=-" * 10)
                    contjogadorvitorias += 1
                    sleep(1)
                else:
                    print("Computador jogou Tesoura")
                    print("EMPATE!")
                    print("-=-" * 10)
                    contempates += 1
                    sleep(1)
    elif op == 2:
        while True:
            print(f"Partidas jogadas: {contpartidas}")
            print(f"Partidas que o jogador venceu: {contjogadorvitorias}")
            print(f"Partidas que o computador venceu: {contcomputadorvitorias}")
            print(f"Partidas empatadas: {contempates}\n")
            op = int(input("Digite 0 para voltar: "))
            system('cls')
            if op == 0:
                break
            else:
                continue
    elif op == 3:
        break
    else:
        continue