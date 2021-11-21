#Crie um programa onde o usuário possa digitara vários valores númericos e cadastre-os em uma lista. Caso o número ja tenha sido digitado, ele não será adicionado.
#No final, serão exibidos todos os valores únicos digitados em ordem crescente.
valores = []
while True:
    num = int(input("Digite um número inteiro: "))
    if num not in valores:
        valores.append(num)
        print("Valor cadastrado com sucesso.")
    else:
        print("Valor já cadastrado. Não irei cadastrar novamente.")
    op = ' '
    while op not in 'SN':
        op = input("Quer continuar [S/N]? ").strip().upper()[0]
    if op == 'N':
        break
valores.sort()
print("-=" * 30)
print(f"Você digitou os seguintes valores: {valores}")