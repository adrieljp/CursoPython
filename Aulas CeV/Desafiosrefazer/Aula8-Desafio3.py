#Escreva um programa que  leia DOIS NÚMEROS inteiros e compare-os, mostrando na tela uma mensagem:
#O primeiro valor é MAIOR.
#O segundo valor é MAIOR.
#NÃO EXISTE valor maior, os dois são IGUAIS.
num1 = int(input("Digite o primero número: "))
num2 = int(input("Digite o segundo número: "))
if num1 > num2:
    print(f"O número {num1} é maior que o número {num2}")
elif num2 > num1:
    print(f"O número {num2} é maior que o número {num1}")
else:
    print(f"Os números {num1} e {num2} são IGUAIS.")