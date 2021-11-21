#Faça um programa que leia um número inteiro qualquer e mostre na tela sua tabuada.
n1=int(input("Digite um número para mostrar sua tabuada: "))
for tabuada in range(1,11):
    total=n1*tabuada
    print("{} x {} = {}".format(str(n1), str(tabuada), str(total)))