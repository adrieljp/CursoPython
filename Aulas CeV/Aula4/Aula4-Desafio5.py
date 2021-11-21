#O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
#Faça um programa que leia o nome dos quatros alunos e mostre a ordem sorteada.
from random import shuffle
al1=input("Digite o nome do primeiro aluno: ")
al2=input("Digite o nome do segundo aluno: ")
al3=input("Digite o nome do terceiro aluno: ")
al4=input("Digite o nome do quarto aluno: ")
lista = [al1, al2, al3, al4]
shuffle(lista)
print("A ordem dos alunos sorteados é {}.".format(lista))