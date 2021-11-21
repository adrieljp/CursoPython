def leiadinheiro(msg):
    ok = False
    while not ok:
        entrada = input(msg).replace(",", ".").strip()
        if entrada.isalpha() or entrada == '':
            print(f"\033[0;31mERRO! \"{entrada}\" é um preço inválido!\033[m")
        else:
            ok = True
            return float(entrada)


def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except(ValueError, TypeError):
            print("\033[31mERRO: Por favor, digite um número inteiro válido.\033[m")
        except(KeyboardInterrupt):
            print("\n\033[31mO usuário preferiu não digitar esse número.\033[m")
            return 0
        else:
            return n


def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except(ValueError, TypeError):
            print("\033[31mERRO: Por favor, digite um número real válido.\033[m")
        except(KeyboardInterrupt):
            print("\n\033[31mO usuário preferiu não digitar esse número.\033[m")
            return 0
        else:
            return n


def leiastr(msg):
    while True:
        try:
            n = str(input(msg))
        except(KeyboardInterrupt):
            print("ERRO! O usuário preferiu não informar o dado.")
        except:
            print("ERRO! Digite uma string válida.")
        else:
            return n

def linha(tam=40):
    return '-' * tam
 

def clear():
    from os import system, name
    if name == 'nt':
        system('cls')
    else:
        system('clear')


def cabecalho(txt):
    print(linha())
    print(txt.center(40))
    print(linha())


def menu(lista):
    cabecalho("MENU PRINCIPAL")
    c = 1 
    for item in lista:
        print(f"{c} - {item}")
        c += 1
    op = leiaint("Sua opção: ")
    return op

