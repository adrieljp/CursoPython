#Dicionário declarado abaixo e print do dicionário inteiro.
pessoas = {'nome':'Adriel', 'sexo':'M', 'idade': 16}
print(pessoas)

#Para mostrar um índice em dicionários, é usado a síntaxe literal, dessa maneira:
print(pessoas['nome'])

#O método abaixo não funcionará porque a síntaxe de um dicionário é literal.
'''print(pessoas[0])'''

#É possível printar apenas as keys do dicionário.
print(pessoas.keys())

#É possível printar apenas os values do dicionário.
print(pessoas.values())

#E é possível printar os items também, que é a junção das keys e dos values.
print(pessoas.items())

#É possível acessar as keys, os values e os items em laços.
#Para acessar as keys:
for k in pessoas.keys():
    print(k)

#Para acessar os values:
for v in pessoas.values():
    print(v)

#Para acessar os items:
for k, v in pessoas.items():
    print(f"{k} = {v}")

#Posso também DELETAR algo do dicionário.
#OBS: Deixei como comentário para não dar erro nos próximos comandos, mas está funcionando corretamente.
'''
del pessoas['sexo']
for k, v in pessoas.items():
    print(f"{k} = {v}")
'''    

#É possível também MUDAR algo do dicionário.
#OBS: Deixei como comentário para não dar erro nos próximos comandos, mas está funcionando corretamente.
'''
pessoas['nome'] = 'Jorge'
for k, v in pessoas.items():
    print(f"{k} = {v}")
'''

#É possível também ADICIONAR algo ao dicionário.
#OBS: Deixei como comentário para não dar erro nos próximos comandos, mas está funcionando corretamente.
'''
pessoas['peso'] = 98.5
for k, v in pessoas.items():
    print(f"{k} = {v}")
'''

#Criando dicionários dentro de uma lista, é possível fazer de dois modos, digitando os dicionários dentro da lista dessa maneira:
#lista[{'uf':'Rio de Janeiro', 'sigla':'RJ'}, {'uf':'São Paulo', 'sigla':'SP'}]
#Ou então usando o append dessa maneira:
brasil = []
estado1 = {'uf':'Rio de Janeiro', 'sigla':'RJ'}
estado2 = {'uf':'São Paulo', 'sigla':'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(estado1)
print(estado2)
print(brasil)

#É possível usar manipulação de strings.
print(brasil[0]) or print(brasil[1])
print(brasil[0]['uf']) or print(brasil[0]['sigla'])
print(brasil[1]['uf']) or print(brasil[1]['sigla'])

#Em dicionários não é possível fazer uma cópia dessa maneira "[:]", para fazer uma cópia em dicionários temos que usar o comando ".copy()".
estado = {}
brasil = []
for c in range(1, 4):
    estado['uf'] = input("Unidade Federativa: ")
    estado['sigla'] = input("Sigla do Estado: ")
    brasil.append(estado.copy())
for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()