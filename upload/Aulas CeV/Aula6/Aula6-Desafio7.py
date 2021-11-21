# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250.00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input("Digite o seu salário: R$"))
if salario >= 1250.00:
    novo = salario + (salario * 10 / 100)
    print("O seu salário era R${:.2f}, teve um aumento de 10 porcento e passou a custar R${:.2f}.".format(salario, novo))
else:
    novo = salario + (salario * 15 / 100)
    print("O seu salário era R${:.2f}, teve um aumento de 15 porcento e passou a custar R${:.2f}.".format(salario, novo))