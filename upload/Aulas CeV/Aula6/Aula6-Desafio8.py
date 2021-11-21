# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
print("-=-" * 20)
print("Analisador de triângulos.")
print("-=-" * 20)
r1 = float(input("Digite o primeiro segmento: "))
r2 = float(input("Digite o segundo segmento: "))
r3 = float(input("Digite o terceiro segmento: "))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("Os valores {:.2f}, {:.2f} e {:.2f} podem formar um triângulo.".format(r1, r2, r3))
else:
    print("Os valores {:.2f}, {:.2f} e {:.2f} não podem formar um triângulo.".format(r1, r2, r3))