#Laço de repetição FOR
for c in range(0, 6):
    print("Oi")
print("FIM")

print("////////////////////////////////////////////")

for c in range(1, 6):
    print(c)

print("////////////////////////////////////////////")

for c in range(6, 0, -1):
    print(c)

print("////////////////////////////////////////////")

for c in range(0, 11, 2):
    print(c)

print("////////////////////////////////////////////")

n = int(input("Digite um número inteiro: "))
for c in range(1, n+1):
    print(c)
print("FIM.")

print("////////////////////////////////////////////")

i = int(input("Inicio: "))
f = int(input("Fim: "))
p = int(input("Passo: "))
for c in range(i, f+1, p):
    print(c)
print("FIM.")

print("////////////////////////////////////////////")

s = 0
for c in range(0, 5):
    n = int(input("Digite um número inteiro: "))
    s += n
print("A soma de todos os valores foi {}".format(s))