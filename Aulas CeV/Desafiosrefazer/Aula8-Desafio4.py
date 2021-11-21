#Faça um programa que leia a data de nascimento de um jovem e informe, de acordo com sua idade:
#Se ele AINDA VAI SE ALISTAR ao serviço militar.
#Se é a HORA DE SE ALISTAR.
#Se ja PASSOU DO TEMPO do alistamento.
#Seu programa deverá também mostrar o tempo que falta ou que passou do prazo.
from datetime import date
from os import system
atual = date.today().year
while True:
    nascimento = int(input("Ano de nascimento [0 para parar]: "))
    system('cls')
    if nascimento == 0:
        break
    idade = atual - nascimento
    if idade < 0 or idade > 110:
        continue
    while True:
        sexo = int(input('''Qual seu sexo?
[ 1 ]Masculino
[ 2 ]Feminino
[ 0 ]Voltar
Informe seu sexo: '''))
        system('cls')
        if sexo == 1:
            print(f"Quem nasceu em {nascimento} tem {idade} anos em {atual}.")
            if idade == 18:
                print("Você tem que se alistar IMEDIATAMENTE.\n")
                break
            elif idade < 18:
                saldo = 18 - idade
                alistamento = nascimento + 18
                print(f"Ainda faltam {saldo} anos para o alistamento.")
                print(f"Seu alistamento será em {alistamento}.\n")
                break
            else:
                saldo = idade - 18
                alistamento = nascimento + 18
                print(f"Você já deveria ter se alistado há {saldo} anos.")
                print(f"Seu alistamento foi em {alistamento}.\n")
                break
        elif sexo == 2:
            print("Você não precisa de alistamento OBRIGATÓRIO.\nCaso queira se alistar, por favor se dirija a recepção para mais informações.\n")
            break
        elif sexo == 0:
            break
        else:
            continue