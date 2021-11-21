#Faça um algortimo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
salario=float(input("Digite o valor do seu salário: R$"))
salario2=salario + (salario * 15 / 100)
print("O seu novo salário com aumento é: {:.2f}".format(salario2))