# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
# Ex: Digite um número 1834
# Unidade: 4
# Dezena: 3
# Centena: 8
# Milhar: 1

num=int(input("Informe um número inteiro de 0 até 9999: "))
unidade = num // 1 % 10
dezena = num // 10 % 10
centena = num // 100 % 10
milhar = num // 1000 % 10
if num <= 9999:
    print("O número escolhido foi {}.\nUnidade: {}.\nDezena: {}.\nCentena: {}.\nMilhar: {}.".format(num, unidade, dezena, centena, milhar))
else:
    print("O número escolhido é maior que 9999.")