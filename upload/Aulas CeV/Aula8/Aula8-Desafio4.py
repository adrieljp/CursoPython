#Faça um programa que leia a data de nascimento de um jovem e informe, de acordo com sua idade:
#Se ele AINDA VAI SE ALISTAR ao serviço militar.
#Se é a HORA DE SE ALISTAR.
#Se ja PASSOU DO TEMPO do alistamento.
#Seu programa deverá também mostrar o tempo que falta ou que passou do prazo.
from datetime import date
atual = date.today().year
nascimento = int(input("Ano de nascimento: "))
idade = atual - nascimento
sexo = int(input('''Qual seu sexo?
[ 1 ] Masculino.
[ 2 ] Feminino.
Escolha sua opção: '''))
if sexo == 1:
    print("Quem nasceu em {} tem {} anos em {}.".format(nascimento, idade, atual))
    if idade == 18:
        print("Você tem que se alistar IMEDIATAMENTE.")
    elif idade < 18:
        saldo = 18 - idade
        ano = atual + saldo
        print("Ainda faltam {} anos para o alistamento.".format(saldo))
        print("Seu alistamento será em {}.".format(ano))
    else:
        saldo = idade - 18
        ano = atual - saldo
        print("Você já deveria ter se alistado há {} anos.".format(saldo))
        print("Seu alistamento foi em {}.".format(ano))
elif sexo == 2:
    print("Você não precisa de alistamento OBRIGATÓRIO.\nCaso queira se alistar, por favor se dirija a recepção para mais informações.")
else:
    print("Opção inválida.")