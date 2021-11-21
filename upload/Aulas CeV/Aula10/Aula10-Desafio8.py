#Crie um programa que leia vários números inteiros pelo teclado. 
#O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
#No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
cont = 0
soma = 0
num = 0
num = int(input("Informe um número inteiro [999] para parar: "))
while num != 999:
        cont += 1
        soma += num
        num = int(input("Informe um número inteiro [999] para parar: "))
print("Foram digitados {} números e a soma entre eles é {}".format(cont, soma))