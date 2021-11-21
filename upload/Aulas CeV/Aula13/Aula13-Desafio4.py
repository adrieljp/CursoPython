#Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
#A) Quantos números foram digitados.
#B) A lista de valores, ordenada de forma descrescente.
#C) Se o valor 5 foi digitado e está ou não na lista.
num = []
while True:
    num.append(int(input("Digite um número: ")))
    op = ' '
    while op not in 'SN':
        op = input("Quer continuar [S/N]? ").strip().upper()[0]
    if op == 'N':
        break
print("=-" * 30)
print(f"Você digitou {len(num)} elementos.")
num.sort(reverse=True)
print("=-" * 30)
print(f"Os valores em ordem decrescente são {num}")
print("=-" * 30)
if 5 in num:
    print("O valor 5 está na lista.")
else:
    print("Não achei o valor 5 na lista.")
print("=-" * 30)