#Faça um programa que leia 5 valores númericos e guarde-os em uma lista.
#No final, mostre qual foi o maior e o menor valor digitado e suas respectivas posições.
valores = []
maior = menor = 0
for c in range(0, 5):
    valores.append(int(input(f"Digite um valor para a posição {c}: ")))
    if c == 0:
        menor = maior = valores[c]
    else:
        if valores[c] > maior:
            maior = valores[c]
        elif valores[c] < menor:
            menor = valores[c]
print(f"Os números digitados foram {valores}")
print(f"O maior valor foi {maior} nas posições ", end='')
for i, v in enumerate(valores):
    if v == maior:
        print(f"{i}... ", end='')
print(f"\nO menor valor foi {menor} nas posições ", end='')
for i, v in enumerate(valores):
    if v == menor:
        print(f"{i}... ", end='')