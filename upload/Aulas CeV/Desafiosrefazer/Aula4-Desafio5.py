#O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
#Faça um programa que leia o nome dos quatros alunos e mostre a ordem sorteada.

'''
from random import shuffle
al1 = input("Digite o nome do primeiro aluno: ").strip().title()
al2 = input("Digite o nome do segundo aluno: ").strip().title()
al3 = input("Digite o nome do terceiro aluno: ").strip().title()
al4 = input("Digite o nome do quarto aluno: ").strip().title()
lista = [al1, al2, al3, al4]
shuffle(lista)
print(f"A ordem sorteada dos alunos: ", end='')
for a in lista:
    print(f"{a}", end=' ')
'''

from random import shuffle

op = int(input("Quantos alunos você quer sortear? "))

lista = []
for c in range(0, op):
    alunos = input(f"Digite o nome do {c+1}º aluno: ").strip().title()
    lista.append(alunos)

shuffle(lista)
print(f"A ordem sorteada dos alunos foi: ", end='')
for a in lista:
    print(f'{a}', end=' ')