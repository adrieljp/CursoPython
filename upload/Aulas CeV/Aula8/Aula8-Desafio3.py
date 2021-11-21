#Escreva um programa que  leia DOIS NÚMEROS inteiros e compare-os, mostrando na tela uma mensagem:
#O primeiro valor é MAIOR.
#O segundo valor é MAIOR.
#NÃO EXISTE valor maior, os dois são IGUAIS.
num1 = int(input("Digite o primeiro valor: "))
num2 = int(input("Digite o segundo valor: "))
if num1 > num2:
    print("O primeiro valor é MAIOR.")
elif num2 > num1:
    print("O segundo valor é MAIOR.")
else:
    print("Os dois valores são IGUAIS.")