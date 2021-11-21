#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
#A média de idade do grupo
#Qual é o nome do homem mais velho
#Quantas mulheres têm menos de 20 anos
somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
mulheres20 = 0
for p in range(1, 5):
    print("----- {}ª PESSOA-----".format(p))
    nome = input("Nome: ").strip().capitalize()
    idade = int(input("Idade: "))
    sexo = input("Sexo [M/F]: ").strip().upper()
    somaidade = idade + idade + idade + idade
    if p == 1 and sexo == 'M':
        maioridadehomem = idade
        nomevelho = nome
    if sexo == "M" and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo == "F" and idade < 20:
        mulheres20 += 1
mediaidade = somaidade / 4
print("A média de idade do grupo é de {} anos".format(mediaidade))
print("O homem mais velho é o {} e tem {} anos.".format(nomevelho, maioridadehomem))
print("Ao todo são {} mulheres com menos de 20 anos.".format(mulheres20)) 