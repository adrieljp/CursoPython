#Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
#Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
from time import sleep
def linha():
    print("-=" * 25)
def maior(* num):
    mai = cont = 0
    linha()
    print("Analisando os valores passados...")
    for n in num:
        print(f"{n} ", end='', flush=True)
        sleep(0.5)
        cont += 1
        if cont == 1:
            mai = n
        else:
            if n > mai:
                mai = n
    print(f"Foram informados {cont} valores ao todo.")
    print(f"O maior valor informado foi {mai}")
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()