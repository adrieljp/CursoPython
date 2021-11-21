#Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
#No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
from time import sleep
ficha = []
while True:
    nome = input("Nome: ")
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    op = ' '
    while op not in "SN":
        op = input("Quer continuar [S/N]? ").strip().upper()[0]
    if op == "N":
        break
print("-=" * 30)
print(f"{'No.':<4}{'NOME':<10}{'MÉDIA':>8}")
print("-" * 26)
for i, a in enumerate(ficha):
    print(f"{i:<4}{a[0]:<10}{a[2]:>8.1f}")
while True:
    print("-" * 35)
    op = int(input("Mostrar notas de qual aluno? (999 interrompe): "))
    if op == 999:
        print("FINALIZANDO...")
        sleep(0.5)
        break
    if op <= len(ficha) - 1:
        print(f"Notas de {ficha[op][0]} são {ficha[op][1]}")
print("<<< VOLTE SEMPRE >>>")