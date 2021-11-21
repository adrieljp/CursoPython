#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#à vista dinheiro/cheque: 10% de desconto
#à vista no cartão: 5% de desconto
#em até 2x no cartão: preço normal 
#3x ou mais no cartão: 20% de juros
preçoproduto = float(input("Digite o valor das compras: R$"))
preçoavista1 = preçoproduto - (preçoproduto * 10 / 100)
preçoavista2 = preçoproduto - (preçoproduto * 5 / 100)
preçocartao = preçoproduto + (preçoproduto * 20 / 100)
pagamento = int(input('''FORMAS DE PAGAMENTO
[ 1 ] À vista dinheiro ou cheque, 10% de desconto.
[ 2 ] À vista no cartão, 5% de desconto.
[ 3 ] Cartão em até 2x, preço normal.
[ 4 ] Cartão em 3x ou mais, 20% de juros.
Escolha a forma de pagamento: '''))
if pagamento == 1:
    print("Sua compra de R${:.2f} vai custar R${:.2f} com o desconto de 10%.".format(preçoproduto, preçoavista1))
elif pagamento == 2:
    print("Sua compra de R${:.2f} vai custar R${:.2f} com o desconto de 5%.".format(preçoproduto, preçoavista2))
elif pagamento == 3:
    parcelas = preçoproduto / 2
    print("Sua compra será parcelada em 2x, terá 2 parcelas de R${:.2f} e irá custar R${:.2f} SEM JUROS.".format(parcelas, preçoproduto))
elif pagamento == 4:
    parcelas = int(input("Quantas parcelas? "))
    parcela = preçocartao / parcelas
    print("Sua compra será parcelada em {}x de R${:.2f} COM JUROS.".format(parcelas, parcela))
    print("Sua compra de R${:.2f} irá custar R${:.2f} no final.".format(preçoproduto, preçocartao))
else:
    print("Opção inválida.")
