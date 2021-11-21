#Crie um programa que leia vários números inteiros pelo teclado. 
#No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
#O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
op = "S"
quant = media = soma = maior = menor = 0
while op == "S":
    num = int(input("Digite um número: "))
    soma += num
    quant += 1
    if quant == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
    op = input("Quer continuar? [S/N]\nSua escolha: ").strip().upper()[0]
media = soma / quant
print("Você digitou {} valores e a média foi {}\nO maior número lido foi {} e o menor número lido foi {}.".format(quant, media, maior, menor))