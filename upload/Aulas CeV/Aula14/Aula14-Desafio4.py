#Aprimore o exercício anterior, mostrando no final:
#A) A soma de todos os valores pares digitados.
#B) A soma dos valores da terceira coluna.
#C) O maior valor da segunda linha.
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapar = somatc = maiorsl = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f"Digite um valor para [{l}, {c}]: "))
print("-=" * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f"[{matriz[l][c]:^5}]", end='')
        if matriz[l][c] % 2 == 0:
            somapar += + matriz[l][c]
    print()
print("-=" * 30)
print(f"A soma dos valores pares é {somapar}")
for l in range(0, 3):
    somatc += + matriz[l][2]
print(f"A soma dos valores da terceira coluna é {somatc}")
for c in range(0, 3):
    if c == 0 or matriz[1][c] > maior:
        maior = matriz[1][c]