#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. 
#Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.
'''
from random import choice
al1 = input("Digite o nome do primeiro aluno: ").strip().title()
al2 = input("Digite o nome do segundo aluno: ").strip().title()
al3 = input("Digite o nome do terceiro aluno: ").strip().title()
al4 = input("Digite o nome do quarto aluno: ").strip().title()
lista = [al1, al2, al3, al4]
alunos = choice(lista)
print(f"O aluno escolhido foi: {alunos}") 
'''

'''
from random import choice

alunos = []
for c in range(1, 5):
    aluno = input(f"Digite o nome do {c}º aluno: ").strip().title()
    alunos.append(aluno)

sorteio = choice(alunos)
print(f'O aluno escolhido foi: {sorteio}')
'''

from random import choice

num = int(input("Quantos alunos você quer sortear? "))
lista = []

for c in range(0, num):
    aluno = input(f"Digite o nome do {c+1}º aluno: ").strip().title()
    lista.append(aluno)

sorteio = choice(lista)
print(f"O aluno escolhido foi {sorteio}.")