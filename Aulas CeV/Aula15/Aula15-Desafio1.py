#Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
#No final, mostre o conteúdo da estrutura na tela.
from os import system
aluno = {}
aluno['Nome'] = str(input("Nome: ")).strip().title()
aluno['Média'] = float(input(f"Média de {aluno['Nome']}: "))
system('cls')
print("-=" * 10)
if aluno['Média'] >= 7:
    aluno['Situação'] = 'aprovado.'
elif 5 <= aluno['Média'] < 7:
    aluno['Situação'] = 'recuperação.'
else:
    aluno['Média'] = 'reprovado.'
for k, v in aluno.items():
    print(f"{k} {v}")
    print('-=' * 10)