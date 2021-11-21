from utilidadescev.dado import *

def arquivoexiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def arquivocriar(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print("Houve um ERRO na criação do arquivo.")
    else:
        print(f"Arquivo {nome} criado com sucesso!")


def lerarquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print("ERRO ao ler o arquivo!")
    else:
        print(linha())
        print("PESSOAS CADASTRADAS".center(40))
        print(linha())
        print(a.read())


def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print("ERRO ao abrir o arquivo!")
    else:
        try:
            a.write(f"{nome} \t\t{idade} anos.\n")
        except:
            print("ERRO na hora de escrever os dados.")
        else:
            print(f"Novo registro de {nome} adicionado.")
            a.close()