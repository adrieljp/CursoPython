#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
ptermo = int(input("Informe o termo: "))
razao = int(input("Informe a razão: "))
decimo = ptermo + (10 - 1) * razao
for c in range(ptermo, decimo + razao, razao):
    print(c)
