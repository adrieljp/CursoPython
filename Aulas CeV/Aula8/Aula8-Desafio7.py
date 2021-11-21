#Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#EQUILÁTERO: todos os lados iguais
#ISÓSCELES: dois lados iguais, um diferente
#ESCALENO: todos os lados diferentes
print("-=-" * 40)
print("Irei analisar se é possível fazer um triângulo e dizer se ele é EQUILÁTERO, ISÓSCELES ou ESCALENO.")
print("-=-" * 40)
r1 = float(input("Digite o primeiro segmento: "))
r2 = float(input("Digite o segundo segmento: "))
r3 = float(input("Digite o terceiro segmento: "))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("Os segmentos acima PODEM FORMAR um triângulo ", end="")
    if r1 == r2 and r2 == r3:
        print("EQUILÁTERO.") 
    elif r1 == r2 or r2 == r3 or r1 == r3:
        print("ISÓSCELES.")
    else:
        print("ESCALENO.")
else:
    print("Os segmentos acima NÃO PODEM formar um triângulo")