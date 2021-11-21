#Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa.
#Retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade <= 15:
        print(f"Com {idade} anos: NÃO VOTA.")
    elif idade == 16 or idade == 17 or idade >= 65:
        print(f"Com {idade} anos: VOTO OPCIONAL.")
    else:
        print(f"Com {idade} anos: VOTO OBRIGATÓRIO.")
ano = int(input("Em que ano você nasceu? "))
voto(ano)