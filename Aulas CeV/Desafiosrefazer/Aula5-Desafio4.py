# Crie um programa que leia o nome inteiro de uma pessoa e diga se ela tem "SILVA" no nome.
nome=input("Digite seu nome completo: ").strip().upper()
check= "SILVA" in nome
print("Seu nome tem silva? {}.".format(check))