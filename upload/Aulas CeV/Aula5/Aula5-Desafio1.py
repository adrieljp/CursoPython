# Crie um programa que leia o nome completo de uma pessoa e mostre: 
# O nome com todas as letras maiusculas.
# O nome com todas as letras minusculas.
# Quantas letras ao todo (sem considerar espaços.)
# Quantas letras tem o primeiro nome.

nome = input("Digite o seu nome completo: ".strip())
nomediv=nome.split()
print("Todas as letras maiusculas: {}".format(nome.upper()))
print("Todas as letras minusculas: {}".format(nome.lower()))
print("Letras ao todo sem considerar espaços: {}".format(len(nome)-nome.count(" ")))
print("O seu primeiro nome é {} e tem {} letras.".format(nomediv[0], len(nomediv[0])))