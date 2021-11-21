#Crie um programa que leia o NOME e o PREÇO de VÁRIOS PRODUTOS.
#O programa deverá perguntar se o USUÁRIO vai continuar.
#No final, mostre:
#Qual é o TOTAL GASTO na compra.
#Quantos produtos custam MAIS de R$1000.
#Qual é o NOME do produto mais barato.
total = maismil = menor = cont = 0
barato = ''
while True:
    produto = input("Nome do produto: ")
    preco = float(input("Preço: R$"))
    cont += 1
    op = ' '
    while op not in "SN":
        op = input("Quer continuar [S/N]? ").strip().upper()[0]
    total += preco
    if preco >= 1000:
        maismil += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    if op == "N":
        break
print("-" * 20, "FIM DO PROGRAMA", "-" * 20)
print(f"O total da compra foi R${total:.2f}")
print(f"Temos {maismil} produtos custando mais de R$1000")
print(f"O produto mais barato foi {barato} custando {menor:.2f}")
