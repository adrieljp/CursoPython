#Crie um programa que leia quanto dinhero uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. Considerando que o valor do dólar é R$3,27.
dinheiro=float(input("Insira o valor da sua carteira: R$"))
usd= dinheiro/3.27
print("Você tem {:.2f} disponível.\nVocê pode comprar {:.2f} dólares americanos.".format(dinheiro, usd))