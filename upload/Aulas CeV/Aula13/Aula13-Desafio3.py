#Crie um programa onde o usuário possa digitar 5 valores númericos e cadastre-os em uma lista, ja na posição correta de inserção (sem usar o sort()).
#No final, mostre a lista ordenada na tela.
valores = []
for c in range(0, 5):
    num = int(input("Digite um valor: "))
    if c == 0 or num > valores[-1]:
        valores.append(num)
        print("Adicionado ao final da lista.")
    else:
        pos = 0
        while pos < len(valores):
            if num <= valores[pos]:
                valores.insert(pos, num)
                print(f"Adicionado na posição {pos} da lista.")
                break
            pos += 1
print("-=" * 30)
print(f"Os valores digitados na ordem foram {valores}")