def clear():
    from os import system, name
    if name == 'nt':
        system('cls')
    else:
        system('clear')


def menu(msg, linha=True, tamanholinha=25, tipolinha='-'):
    if linha:
        print(tipolinha * tamanholinha)
        print(msg.center(tamanholinha))
        print(tipolinha * tamanholinha)
    else:
        print(msg)


def leiastr(msg):
    while True:
        try:
            string = str(input(msg)).strip().upper()[0]
        except:
            continue
        else:
            return string


def logica():
    from random import randint
    dado = randint(1, 6)
    while True:
        dado = randint(1, 6)
        op = leiastr('Você gostaria de jogar o dado [S/N]? ')
        if op == 'N':
            clear()
            break
        elif op == 'S':
            print(f'{dado}\n')

clear()
menu('DADOS VIRTUAIS', linha=True, tamanholinha=20, tipolinha='-')
logica()