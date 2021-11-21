#Faça um programa que leia um número inteiro qualquer e mostre na tela sua tabuada.
n1 = int(input("Digite um número para mostrar sua tabuada: "))
print("-=" * 15)
for tabuada in range(1, 11):
    resultado = n1 * tabuada
    print(f"{n1} x {tabuada} = {resultado}")
print("-=" * 15)