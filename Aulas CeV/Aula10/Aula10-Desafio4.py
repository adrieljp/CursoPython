#Faça um programa que leia um número qualquer e mostre o seu fatorial.
#Exemplo:
#5! = 5 x 4 x 3 x 2 x 1 = 120
num = int(input("Digite um número: "))
cont = num
fatorial = 1
print("Calculando {}! ".format(num), end='')
while cont > 0:
    print("{}".format(cont), end='')
    if cont > 1:
        print(" x ", end='')
    else:
        print(" = ", end='')
    fatorial *= cont
    cont -= 1
print("{}".format(fatorial))
