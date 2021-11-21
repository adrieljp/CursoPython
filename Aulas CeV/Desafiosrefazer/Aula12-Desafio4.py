#Desenvolva um programa que leia QUATRO VALORES pelo teclado e guarde-os em uma tupla. No final mostre:
#A) Quantas vezes apareceu o valor 9.
#B) Em que posição foi digitado o primeiro valor 3.
#C) Quais foram os números pares.
num = (int(input("Digite um número: ")), int(input("Digite outro número: ")), int(input("Digite outro número: ")), int(input("Digite outro número: ")))
print("Os números lidos foram ", end='')
for n in num:
    print(n, end=' ')
print(f"\nO número 9 aparece {num.count(9)} vezes.")
if 3 in num:
    print(f"O número 3 aparece na {num.index(3)+1}ª posição.")
else:
    print("O número 3 não foi digitado.")
print(f"Os valores pares digitados foram ", end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')
print("\nObrigado por ter usado o programa.")