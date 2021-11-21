#Crie um programa que gerencie o aproveitamento de um jogador de futebol.
#O programa vai ler o nome do jogador e quantas partidas ele jogou.
#Depois vai ler a quantidade de gols feitos em cada partida.
#No final,tudo isso será guardado em um dicionário incluindo o total de gols feitos durante o campeonato.
from os import system
jogador = {}
partidas = []
soma = 0
jogador['Nome'] = input("Nome do jogador: ").strip().title()
total = int(input(f"Quantas partidas {jogador['Nome']} jogou? "))
for p in range(total):
    jogador['Gols'] = int(input(f"Quantos gols na partida {p + 1}? "))
    soma += jogador['Gols']
    partidas.append(jogador['Gols'])
system('cls')
jogador['Gols'] = partidas
jogador['Total'] = soma
print("-=" * 30)
print(jogador)
print("-=" * 30)
for k, v in jogador.items():
    print(f"{k}: {v}")
print("-=" * 30)
print(f"O jogador {jogador['Nome']} jogou {total} partidas.")
for i, v in enumerate(partidas):
    print(f"Na partida {i + 1}, fez {v} gols.")
print(f"Foi um total de {jogador['Total']} gols.")