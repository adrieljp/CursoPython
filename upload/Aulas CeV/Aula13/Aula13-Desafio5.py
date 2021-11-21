#Crie um programa que vai ler vários números e colocar em uma lista.
#Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores impares digitados, respectivamente.
#Ao final, mostre o conteúdo das três listas geradas.
total = []
pares = []
impares = []
while True:
    num = int(input("Digite um número inteiro: "))
    if num % 2 == 0:
        pares.append(num)
        total.append(num)
    else:
        impares.append(num)
        total.append(num)
    op = ' '
    while op not in "SN":
        op = input("Quer continuar [S/N]? ").strip().upper()[0]
    if op == "N":
        break
print("-=" * 30)
print(f"A lista completa é {total}")
print(f"A lista de pares é {pares}")
print(f"A lista de ímpares é {impares}")
print("-=" * 30)