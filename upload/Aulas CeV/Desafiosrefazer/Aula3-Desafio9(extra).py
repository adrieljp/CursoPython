#Faça um algortimo que leia o salário de um funcionário e mostre seu novo salário, com menos 3% de impostos e com 15% de aumento.
salario = float(input("Informe seu salário: R$"))
desconto = (salario * 3) / 100
salario2 = salario - desconto
aumento = (salario2 * 15) / 100
salariofinal = salario2 + aumento 
print(f"O seu salário é R${salario:.2f}")
print(f"O seu salário com 3% descontados de impostos e com 15% de aumento passa a ser R${salariofinal:.2f}")