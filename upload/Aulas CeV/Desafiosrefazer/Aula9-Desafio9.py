#Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date
atual = date.today().year
maior = 0
menor = 0
for c in range(1, 8):
    ano = int(input("Informe o ano de nascimento da pessoa {}: ".format(c)))
    idade = atual - ano
    if idade >= 21:
        maior += 1 
    else:
        menor += 1 
print("Das 7 pessoas informadas, {} são maiores de idade e {} são menores de idade.".format(maior, menor))