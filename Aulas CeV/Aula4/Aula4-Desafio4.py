#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. 
#Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.
from random import choice
al1=input("Digite o nome do primeiro aluno: ")
al2=input("Digite o nome do segundo aluno: ")
al3=input("Digite o nome do terceiro aluno: ")
al4=input("Digite o nome do quarto aluno: ")
lista = [al1, al2, al3, al4]
aluno = choice(lista)
print("O aluno escolhido foi {}.".format(aluno))