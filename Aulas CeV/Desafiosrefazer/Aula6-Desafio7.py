# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250.00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.
salario = float(input("Informe seu salário: R$"))
if salario > 1250:
    aumento = (salario * 10) / 100
    novosalario = salario + aumento
    print(f"O seu salário era de R${salario:.2f}, com um aumento de 10% (R${aumento:.2f}), o seu novo salário passa a ser R${novosalario:.2f}")
else:
    aumento = (salario * 15) / 100
    novosalario = salario + aumento
    print(f"O seu salário era de R${salario:.2f}, com um aumento de 15% (R${aumento:.2f}), o seu novo salário passa a ser R${novosalario:.2f}")