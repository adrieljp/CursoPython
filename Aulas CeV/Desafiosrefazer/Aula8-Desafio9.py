#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#à vista dinheiro/cheque: 10% de desconto
#à vista no cartão: 5% de desconto
#em até 2x no cartão: preço normal 
#3x ou mais no cartão: 20% de juros
from os import system
while True:
    preco = float(input("Informe o preço do produto [0 para sair]: R$"))
    if preco == 0:
        break
    while True:
        formapagamento = int(input('''\nEscolha a forma de pagamento
[ 1 ]À vista dinheiro/cheque: 10% de desconto
[ 2 ]À vista no cartão: 5% de desconto
[ 3 ]Em até 2x no cartão: preço normal
[ 4 ]3x ou mais no cartão: 20% de juros
[ 5 ]Voltar para o outro menu
Sua escolha: '''))
        system('cls')
        if formapagamento == 1:
            desconto = preco * 10 / 100
            precodesconto = preco - desconto
            print(f"Preço antes do desconto: R${preco:.2f}\nPreço que irá ser pago depois do desconto de 10%: R${precodesconto:.2f}\n")
        elif formapagamento == 2:
            desconto = preco * 5 / 100
            precodesconto = preco - desconto
            print(f"Preço antes do desconto: R${preco:.2f}\nPreço que irá ser pago depois do desconto de 5%: R${precodesconto:.2f}\n")
        elif formapagamento == 3:
            print(f"Preço a ser pago: R${preco:.2f}\n")
        elif formapagamento == 4:
            aumento = preco * 20 / 100
            precoaumento = preco + aumento
            print(f"Preço antes do aumento: R${preco:.2f}\nPreço que irá ser pago depois do aumento de 20%: R${precoaumento:.2f}\n")
        elif formapagamento == 5:
            break
        else:
            continue
            print("\nOPÇÃO INVÁLIDA.")