#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
#Calcule e mostre o comprimento da hipotenusa.
from math import hypot
oposto=float(input("Digite o comprimento do cateto oposto: "))
adjacente=float(input("Digite o comprimento do cateto adjacente: "))
hipotenusa=hypot(oposto, adjacente)
print("Apartir do valor do cateto oposto {} e do cateto adjacente {}.\nO comprimento da hipotenusa é {:.2f}.".format(oposto, adjacente, hipotenusa))