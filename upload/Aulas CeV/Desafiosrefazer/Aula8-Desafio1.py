#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
#O programa vai perguntar o VALOR DA CASA, o SALÁRIO do comprador e em QUANTOS ANOS ele vai pagar.
#Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.
valorcasa = float(input("Qual o valor da casa? R$"))
salario = float(input("Qual o salário do comprador? R$"))
anos = float(input("Em quantos anos será pago? "))
meses = anos * 12
prestacao = valorcasa / meses
porcentagem = (salario * 30) / 100
print(f"Para pagar a casa no valor de R${valorcasa:.2f} em {anos:.0f} anos, o valor das prestções irão ser de R${prestacao:.2f}")
if prestacao > porcentagem:
    print("Desculpe, o empréstimo foi NEGADO pois a parcela excedeu 30% do seu salário.")
else:
    print("Empréstimo APROVADO!")