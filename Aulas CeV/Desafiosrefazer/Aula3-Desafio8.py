#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
preco1 = float(input("Digite o preço do produto: R$"))
desconto = (preco1 * 5) / 100
novopreco = preco1 - desconto
print(f"O preço original é R${preco1:.2f}")
print(f"Você recebeu um desconto de 5% e irá pagar R${novopreco:.2f}")