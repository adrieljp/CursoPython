#A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
#Até 9 anos: Mirim
#Até 14 anos: Infantil
#Até 19 anos: Junior
#Até 25 anos: Sênior
#Acima: Master
from datetime import date
atual = date.today().year
nasc = int(input("Digite seu ano de nascimento: "))
idade = atual - nasc
if idade < 0:
    print("Opção inválida.")
elif idade <= 9:
    print("O atleta tem {} anos.".format(idade))
    print("Classificação: Mirim.")
elif idade <= 14:
    print("O atleta tem {} anos.".format(idade))
    print("Classificação: Infantil.")
elif idade <= 19:
    print("O atleta tem {} anos.".format(idade))
    print("Classificação: Junior.")
elif idade <= 25:
    print("O atleta tem {} anos.".format(idade))
    print("Classificação: Sênior.")
else:
    print("O atleta tem {} anos.".format(idade))
    print("Classificação: Master.")
