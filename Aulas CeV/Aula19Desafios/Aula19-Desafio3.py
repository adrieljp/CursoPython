#Vamos criar um menu em Python, usando modularização.
from utilidadescev.arquivo import *
from utilidadescev.dado import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoexiste(arq):
    arquivocriar(arq) 
while True:
    op = menu(["Ver pessoas cadastradas", "Cadastrar nova pessoa", "Sair do sistema"])
    clear()
    if op == 1:
        while True:
            lerarquivo(arq)
            op = leiaint("\nDigite 0 para voltar: ")
            clear()
            if op == 0:
                break
            else:
                continue
    elif op == 2:
        while True:
            cabecalho("NOVO CADASTRO")
            nome = leiastr("Nome: ").strip().title()
            idade = leiaint("Idade: ")
            cadastrar(arq, nome, idade)
            break
    elif op == 3:
        cabecalho("Saindo do sistema... Até logo!")
        break
    else:
        print("\033[31mERRO! Digite uma opção válida.\033[m")