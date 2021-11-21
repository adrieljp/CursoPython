#Crie um programa que leia a IDADE e o SEXO de várias pessoas.
#A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
#No final, mostre:
#A) Quantas pessoas tem mais de 18 ANOS.
#B) Quantos HOMENS foram cadastrados.
#C) Quantas MULHERES tem menos de 20 ANOS.
homens = pessoas18 = mulheres20 = 0
while True:
    print("-" * 20)
    print("CADASTRE UMA PESSOA")
    print("-" * 20)
    idade = int(input("Idade: "))
    sexo = ' '
    while sexo not in "MF":
        sexo = input("Sexo [M/F]: ").strip().upper()[0]
    op = ' '
    while op not in "SN":
        op = input("Quer continuar [S/N]? ").strip().upper()[0]
    print("-" * 20)
    if idade >= 18:
        pessoas18 += 1
    if sexo == "M":
        homens += 1
    elif sexo == "F" and idade < 20:
        mulheres20 += 1
    if op == "N":
        break
print("=" * 7, "FIM DO PROGRAMA", "=" * 7)
print(f"Total de pessoas com mais de 18 anos: {pessoas18}")
print(f"Ao todo temos {homens} homens cadastrados.")
print(f"Temos {mulheres20} mulheres com menos de 20 anos.")