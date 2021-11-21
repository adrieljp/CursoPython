#Aprimore o desafio 4 para que funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
from os import system
jogador = {}
partidas = []
time = []
soma = 0
while True:
    jogador.clear()
    jogador['Nome'] = input("Nome do jogador: ").strip().title()
    total = int(input(f"Quantas partidas {jogador['Nome']} jogou? "))
    partidas.clear()
    for p in range(total):
        partidas.append(int(input(f"Quantos gols na partida {p + 1}? ")))
    jogador['Gols'] = partidas[:]
    jogador['Total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        op = input("Quer continuar [S/N]? ").strip().upper()[0]
        if op in 'SN':
            break
        print("ERRO! Responda apenas com S ou N.")
    if op == 'N':
        break
system('cls')
print("-=" * 30)
print("cod ", end='')
for i in jogador.keys():
    print(f"{i:<15}", end='')
print()
print("-" * 40)
for k, v in enumerate(time):
    print(f"{k:>3} ", end='')
    for d in v.values():
        print(f"{str(d):<15}", end='')
    print()
print("-" * 40)
while True:
    busca = int(input("Mostrar dados de qual jogador? (999 para parar) "))
    if busca == 999:
        break
    elif busca >= len(time):
        print(f"ERRO! Não existe jogador com código {busca}!")
    else:
        print(f"LEVANTATAMENTO DO JOGADOR {time[busca]['Nome']}.")
        for i, g in enumerate(time[busca]['Gols']):
            print(f"No jogo {i+1} fez {g} gols.")
    print("-" * 40)
print("VOLTE SEMPRE!")