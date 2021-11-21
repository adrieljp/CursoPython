#Faça um algortimo que leia o salário de um funcionário e mostre seu novo salário, com menos 3% de impostos e com 15% de aumento.
salario=float(input("Digite o valor do seu salário: "))
salario2=salario - (salario * 3 / 100)
salario3=salario2 + (salario2 * 15 / 100)
print("O seu novo salário é: {:.2f}".format(salario3))