#Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
#A primeira função vai sortear 5 números e vai colocá-los dentro da lista 
#A segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
from random import randint
from time import sleep
numeros = []
def sorteia():
    print("Sorteando 5 valores da lista: ", end='')
    for c in range(1, 6):
        sorteio = randint(1, 10)
        numeros.append(sorteio)
        print(f"{sorteio} ", end='', flush=True)
        sleep(0.5)
    print("PRONTO!")
def somaPar():
    soma = 0
    for k, v in enumerate(numeros):
        if v % 2 == 0:
            soma += v
    print(f"Somando os valores pares de {numeros}, temos {soma}")
sorteia()
somaPar()