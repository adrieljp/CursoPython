#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
from math import sin, cos, tan, radians
angulo = float(input("Informe um ângulo: "))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print(f"O ângulo de {angulo} tem:\nO seno de {seno:.2f}.\nO cosseno de {cosseno:.2f}.\nE o tangente de {tangente:.2f}.")