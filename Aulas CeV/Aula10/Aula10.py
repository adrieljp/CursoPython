'''for c in range(1, 11):
    print(c)
print("FIM")'''

c = 1
while c < 11:
    print(c)
    c += 1
print("FIM")

print("/////////////////////////////////////////////////")

n = 1
while n != 0:
    n = int(input("Digite um valor: "))
print("FIM")

print("/////////////////////////////////////////////////")

r = "S"
while r == "S":
    n = int(input("Digite um valor: "))
    r = input("Quer continuar? [S/N]: ").upper()
print("FIM")

print("/////////////////////////////////////////////////")

n = 1
par = 0
impar = 0
cont = 0
while n != 0:
    n = int(input("Digite um valor: "))
    if n != 0:
        cont += 1
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print(f"Você digitou {cont} números e deles, {par} eram números pares e {impar} eram números ímpares.")