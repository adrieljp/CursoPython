#Faça um programa que leia o nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
#A) Quantas pessoas foram cadastradas.
#B) Uma listagem com as pessoas mais pesadas.
#C) Uma listagem com as pessoas mais leves.
temp = []
princ = []
maior = menor = 0
while True:
    temp.append(input("Nome: ").strip().capitalize())
    temp.append(float(input("Peso: ").strip()))
    if len(princ) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        elif temp[1] < menor:
            menor = temp[1]
    princ.append(temp[:])
    temp.clear()
    op = ' '
    while op not in "SN":
        op = input("Quer continuar [S/N]? ").strip().upper()[0]
    if op == "N":
        break
print("-=" * 35)
print(f"Ao todo você cadastrou {len(princ)} pessoas.")
print(f"O maior peso foi de {maior:.2f}Kg. Peso de ", end='')
for p in princ:
    if p[1] == maior:
        print(f"[{p[0]}] ", end='')
print(f"\nO menor peso foi de {menor:.2f}Kg. Peso de ", end='')
for p in princ:
    if p[1] == menor:
        print(f"[{p[0]}] ", end='')
