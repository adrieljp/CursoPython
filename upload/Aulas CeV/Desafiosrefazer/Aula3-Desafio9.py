#Faça um algortimo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
salario = float(input("Informe seu salário: R$"))
aumento = (salario * 15) / 100
novosalario = salario + aumento
print(f"Seu salário é de R${salario:.2f}")
print(f"Você recebeu um aumento e seu salário passa a ser R${novosalario:.2f}")