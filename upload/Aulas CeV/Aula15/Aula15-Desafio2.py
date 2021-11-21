#Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
#Guarde esses resultados em um dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
from random import randint
from time import sleep
from operator import itemgetter
jogadores = {'Jogador 1': randint(1, 6),
             'Jogador 2': randint(1, 6),
             'Jogador 3': randint(1, 6),
             'Jogador 4': randint(1, 6)}
ranking = []
print("Valores sorteados:")
for k, v in jogadores.items():
    print(f"{k} tirou {v} no dado.")
    sleep(0.85)
print("-=" * 25)
print("== RANKING DOS JOGADORES ==")
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f"{i+1}º lugar: {v[0]} com {v[1]}")