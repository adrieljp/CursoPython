#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
#O programa vai perguntar o VALOR DA CASA, o SALÁRIO do comprador e em QUANTOS ANOS ele vai pagar.
#Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

casa = float(input("Qual o valor da casa? R$"))
salario = float(input("Qual o seu salário? R$"))
anos = int(input("Em quantos anos você gostaria de pagar? "))
parcela = casa / (anos * 12)
minimo = salario * 30 / 100
print("Para pagar a casa no valor de R${:.2f} em {} anos, o valor das prestações irão ser de R${:.2f}.".format(casa, anos, parcela))
if parcela <= minimo:
    print("Empréstimo aprovado.")
else:
    print("Desculpe, o empréstimo foi negado pois a parcela excedeu 30% do seu salário.")
