#Crie um programa que tenha uma TUPLA totalmente preenchida com uma contagem por extenso, de ZERO até VINTE.
#Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por EXTENSO.
#Pergunte ao usuário se ele quer ou não continuar a digitar números.
from time import sleep
numeros = ("zero", "um", "dois", "três", "quatro",
"cinco", "seis", "sete", "oito", "nove",
"dez", "onze", "doze", "treze", "quatorze",
"quinze", "dezesseis", "dezessete", "dezoito",
"dezenove", "vinte")
while True:
    num = int(input("Digite um número inteiro de 0 a 20: "))
    if 0 <= num <= 20:
        print(f"Você digitou o número {numeros[num]}.")
        sleep(0.8)
        op = ' '
        while op not in 'S/N':
            op = input("Você gostaria de continuar [S/N]? ").strip().upper()[0]
        if op == 'N':
            break
    else:
        print("Tente novamente. ", end='')
print("Obrigado por ter usado esse programa.")