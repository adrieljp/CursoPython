#Crie um código em Python que teste se o site pudim está acessível pelo computador usado.
import urllib.request
try:
    site = urllib.request.urlopen("http://www.pudim.com.br")
except:
    print("O site pudim não está acessível no momento.")
else:
    print("Consegui acessar o site Pudim com sucesso!")