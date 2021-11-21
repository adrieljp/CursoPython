#Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date
maior = menor = 0
atual = date.today().year
for p in range(1, 8):
    ano = int(input(f"Informe o ano de nascimento da {p}º pessoa: "))
    idade = atual - ano
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print(f"Das 7 pessoas informadas, {maior} são maiores de idade e {menor} são menores de idade.")