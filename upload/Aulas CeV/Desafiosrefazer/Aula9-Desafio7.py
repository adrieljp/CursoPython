#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
num = int(input("Informe um número inteiro: "))
total = 0
for c in range(1, num + 1):
    if num % c == 0:
        total += 1
        print("\033[33m", end='')
    else:
        print("\033[31m", end='')
    print("{} ".format(c), end='')
print("\n\033[mO número {} foi divisível {} vezes.".format(num, total))
if total == 2:
    print("O número {} é PRIMO.".format(num))
else:
    print("O número {} NÃO é PRIMO.".format(num))