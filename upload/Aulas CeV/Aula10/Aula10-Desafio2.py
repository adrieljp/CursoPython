#Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. 
#Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
from random import randint
palpites = 0
computador = randint(0, 10)
acertou = False
print("Acabei de pensar em um número entre 0 e 10.")
while not acertou:
    jogador = int(input("Qual seu palpite? "))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print("PERTO! É um número maior que isso.")
        elif jogador > computador:
            print("PERTO! É um número menor que isso.")
print(f"Você acertou com {palpites} tentativas. Parabéns!")