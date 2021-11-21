from time import sleep
cont = 0
while True:
    print(cont, ' >> ', end='')
    cont += 1
    sleep(0.01)
    if cont == 251:
        break
print("Acabou")

print("//////////////////////////////////////")

n = s = cont = 0
while True:
    n = int(input("Digite um número: "))
    if n == 999:
        break
    s += n
    cont += 1
print("Você digitou {} valores e a soma entre eles é {}.".format(cont, s))