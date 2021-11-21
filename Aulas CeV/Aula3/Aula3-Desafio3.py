#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua média.
nota1=float(input("Digite a primeira nota: "))
nota2=float(input("Digite a segunda nota: "))
nota3=(nota1+nota2)/2
print("A média das notas {:.1f} e {:.1f} é {:.1f}.".format(nota1, nota2, nota3))