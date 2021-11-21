#Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
#No final, mostre:
#A)Quantas pessoas foram cadastradas
#B)A média de idade do grupo.
#C)Uma lista com todas as mulheres.
#D)Uma lista com todas as pessoas com idade acima da média.
pessoas = {}
mediaidade = somaidade = cont = 0
galera = []
while True:
    pessoas.clear()
    pessoas['Nome'] = input("Nome: ").strip().title()
    while True:
        pessoas['Sexo'] = input("Sexo [M/F]: ").strip().upper()[0]
        if pessoas['Sexo'] in 'MF':
            break
        print("ERRO! Por favor, digite apenas M ou F.")
    pessoas['Idade'] = int(input("Idade: "))
    galera.append(pessoas.copy())
    somaidade += pessoas['Idade']
    cont += 1
    while True:
        op = input("Quer continuar [S/N]? ").strip().upper()[0]
        if op in 'SN':
            break
        print("ERRO! Responda apenas com S ou N.")
    if op == 'N':
        break
print(f"A) Ao todo temos {len(galera)} pessoas cadastradas.")
mediaidade = somaidade / cont
print(f"B) A média de idade é de {mediaidade:.2f} anos.")
print(f"C) As mulheres cadastradas foram ", end='')
for p in galera:
    if p['Sexo'] == 'F':
        print(f"{p['Nome']} ", end='')
print("\nD) Lista de pessoas que estão acima da média:")
for p in galera:
    if p['Idade'] >= mediaidade:
        print(f"Nome = {p['Nome']}; Sexo = {p['Sexo']}; Idade = {p['Idade']};")
print("<< ENCERRADO >>")