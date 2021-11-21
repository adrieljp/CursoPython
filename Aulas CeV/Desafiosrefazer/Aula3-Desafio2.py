#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
'''
n1=float(input("Digite um número: "))
dobro=n1*2
triplo=n1*3
raiz=n1**(1/2)
print("O valor escolhido foi: {}.".format(n1))
print("O dobro do valor escolhido é: {}.".format(dobro))
print("O triplo do valor escolhido é: {}.".format(triplo))
print("A raiz quadrada do valor escolhido é: {}.".format(raiz))
'''

from math import sqrt
num = float(input("Digite um número: "))
dobro = num * 2
triplo = num * 3
raiz = sqrt(num)
print(f"O valor escolhido foi: {num:.2f}")
print(f"O dobro do valor escolhido é: {dobro:.2f}")
print(f"O triplo do valor escolhido é: {triplo:.2f}")
print(f"A raiz do valor escolhido é: {raiz:.2f}")