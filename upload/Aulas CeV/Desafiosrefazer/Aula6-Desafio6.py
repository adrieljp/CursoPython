#Faça um programa que leia três números e mostre qual é o MAIOR e qual é o MENOR.
a=int(input("Digite o primeiro valor: "))
b=int(input("Digite o segundo valor: "))
c=int(input("Digite o terceiro valor: "))
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print("O maior valor foi {}.".format(maior))
print("O menor valor foi {}.".format(menor))