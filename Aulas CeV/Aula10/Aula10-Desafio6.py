#Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. 
#O programa encerrará quando ele disser que quer mostrar 0 termos.
print("Gerador de PA")
print("-=" * 10)
primeiro = int(input("Primeiro termo: "))
razao = int(input("Razão: "))
termo = primeiro
cont = 1
termos = 10
total = 0
while termos != 0:
    total = total + termos 
    while cont <= total:
        print("{} >> ".format(termo), end='')
        cont += 1
        termo += razao
    print("PAUSA")
    termos = int(input("Você gostaria de mostrar mais alguns termos? Se sim, digite a quantidade de termos ou então digite 0 para sair.\nEscolha: "))
print("FIM. A PA terminou com {} termos mostrados.".format(total))