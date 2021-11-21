# Faça um programa que leia o nome completo de uma pessoa e mostre o primeiro e o ultimo nome separadamente. EX:
# Nome: Ana Maria de Souza
# Primeiro nome: Ana
# Ultimo nome: Souza
nome=input("Digite seu nome completo: ")
inteiro = nome.split()
print("O seu primeiro nome é {}.\nE o seu ultimo nome é {}.".format(inteiro[0], inteiro[len(inteiro)-1]))