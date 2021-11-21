#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
valor_produto=float(input("Digite o valor do produto: R$"))
valor_descontado=valor_produto - (valor_produto * 5 / 100)
print("O valor original é {:.2f}\nO valor com desconto é: {:.2f}".format(valor_produto, valor_descontado))