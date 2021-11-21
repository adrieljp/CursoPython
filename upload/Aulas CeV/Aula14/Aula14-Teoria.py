#Listas (PARTE 2)
#Criando uma lista dentro de outra lista.
dados = []
pessoas = []
dados.append('Pedro')
dados.append(25)
dados.append('Maria')
dados.append(19)
dados.append('João')
dados.append(32)
pessoas.append(dados[:]) #Essa formula faz uma copia da lista.
print(dados, pessoas)

#Pode ser feito da seguinte maneira também

pessoas=[['Pedro', 25], ['Maria', 19], ['João', 32]]

#Quando uma lista composta é criada, acontece que cada pessoa com sua idade se torna 0, 1, 2...

print(pessoas[0][0]) #Esse comando irá pegar o primeiro índice que seria "Pedro" e sua idade, porém o segundo "[0]" indica que irá ser pego apenas o nome "Pedro"
print(pessoas[1][1])
print(pessoas[2][0])