# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
print("-=-" * 10)
print("ANALISADOR DE TRIÂNGULOS")
print("-=-" * 10)
r1 = float(input("Primeiro segmento: "))
r2 = float(input("Segundo segmento: "))
r3 = float(input("Terceiro segmento: "))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print(f"Os segmentos seguintes PODEM formar um triângulo: {r1}, {r2} e {r3}")
else:
    print(f"Os segmentos seguintes NÃO PODEM formar um triângulo: {r1}, {r2} e {r3}")