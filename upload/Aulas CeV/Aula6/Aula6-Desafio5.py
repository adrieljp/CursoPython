# Faça um programa que ele leia uma no qualquer e mostre se ele é BISSEXTO ou não.
from datetime import date
ano = int(input("Digite um ano para análise ou digite 0 para analisar o ano atual: "))

if ano == 0:
    ano = date.today().year 
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print("O ano {} é BISSEXTO.".format(ano))  
else:
    print("O ano {} NÃO é BISSEXTO.".format(ano))