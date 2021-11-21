#Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. 
#Seu programa tem que realizar três contagens através da função criada:
#A) de 1 até 10, de 1 em 1
#B) de 10 até 0, de 2 em 2
#C) uma contagem personalizada
from time import sleep
def linha():
    print("-=" * 20)
def contador(i, f, p):
    if p < 0:
        p *= -1
    elif p == 0:
        p = 1
    linha()
    print(f"Contagem de {i} até {f} de {p} em {p}")
    if i < f:
        cont = i
        while cont <= f:
            print(f"{cont} ", end='', flush=True)
            sleep(0.5)
            cont += p
        print("FIM!")
    else:
        cont = i
        while cont >= f:
            print(f"{cont} ", end='', flush=True)
            sleep(0.5)
            cont -= p
        print("FIM")
    
contador(1, 10, 1)
contador(10, 0, 2)
linha()
print("Agora é sua vez de personalizar a contagem!")
inicio = int(input("Início: "))
fim = int(input("Fim: "))
passo = int(input("Passo: "))
contador(inicio, fim, passo)