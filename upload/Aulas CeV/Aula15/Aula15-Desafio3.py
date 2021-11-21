#Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os(com idade) em um dicionário.
#Se por acaso o CTPS for diferente de zero, o dicionário receberá também o ano de contratação e o salário.
#Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
from datetime import date
from os import system
pessoas = {}
atual = date.today().year
while True:
    pessoas['Nome'] = input("Nome: ").strip().title()
    nascimento = int(input("Ano de nascimento: "))
    pessoas['Idade'] = atual - nascimento
    pessoas['CTPS'] = int(input("Carteira de Trabalho [0 não tem]: "))
    if pessoas['CTPS'] == 0:
        system('cls')
        print("=-" * 15)
        for k, v in pessoas.items():
            print(f"{k}: {v}")
        break
    else:
        pessoas['Contratação'] = int(input("Ano de contratação: "))
        pessoas['Salário'] = float(input("Salário: R$"))
        pessoas['Aposentadoria'] = pessoas['Idade'] + ((pessoas['Contratação'] + 35) - atual)
        system('cls')
        print("=-" * 15)
        for k, v in pessoas.items():
            print(f"{k}: {v}")
        break