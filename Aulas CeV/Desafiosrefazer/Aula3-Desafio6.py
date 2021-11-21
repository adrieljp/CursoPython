#Crie um programa que leia quanto dinhero uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. Considerando que o valor do dólar é R$3,27.
dinheiro = float(input("Informe o valor do seu dinheiro: R$"))
usd = dinheiro / 3.27
print(f"Você tem R${dinheiro:.2f} e pode comprar ${usd:.2f}")