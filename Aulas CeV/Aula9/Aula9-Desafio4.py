#Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
num = int(input("Digite um número para mostrar sua tabuada: "))
print("-" * 15)
for tabuada in range(1, 11):
    total = num * tabuada
    print("{} x {} = {}".format(num, tabuada, total))
print("-" * 15)