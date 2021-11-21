#Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular(largura e comprimento) e mostre a área do terreno.
def área(l, c):
    área = l * c
    print(f"A área de um terreno {l:.2f}x{c:.2f} é de {área:.2f}m²")
l = float(input("LARGURA (m): "))
c = float(input("COMPRIMENTO (m): "))
área(l, c)