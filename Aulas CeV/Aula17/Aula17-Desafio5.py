#Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
#– Quantidade de notas
#– A maior nota
#– A menor nota
#– A média da turma
#– A situação (opcional)
resp = {}
def notas(* tot, sit=False):
    cont = total = maior = menor = media = soma = 0
    for nota in tot:
        cont += 1
        soma += nota
        if cont == 1:
            maior = nota
            menor = nota
        else:
            if nota > maior:
                maior = nota
            elif nota < menor:
                menor = nota
    total = cont
    resp['Total'] = total
    resp['Maior'] = maior
    resp['Menor'] = menor
    media = soma / cont
    resp['Média'] = media
    if sit == True:
        if media >= 7:
            resp['Situação'] = 'BOM'
        elif 5 <= media < 7:
            resp['Situação'] = 'RAZOÁVEL'
        else:
            resp['Situação'] = 'RUIM'
notas(3, 5, 10, 7, sit=True)
for k, v in resp.items():
    print(k, v)