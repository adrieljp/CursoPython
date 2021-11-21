# Crie um programa que leia um número inteiro e mostre na tela se ele é IMPAR ou PAR.
num = int(input("Digite um número: "))
if num % 2 == 0:
    print(f"O número {num} é PAR.")
else:
    print(f"O número {num} é ÍMPAR.")