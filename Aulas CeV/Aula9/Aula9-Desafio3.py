#Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500.
s = 0
contador = 0
for n in range(1, 501, 2):
    if n % 3 == 0:
        contador = contador + 1
        s = s + n
print("A soma dos múltiplos de três no intervalo de 1 até 500 que são {} números, a soma de todos eles da o resultado de {}.".format(contador, s))