#Dicionários
#Para declarar um dicionário pode ser usado "{}" ou o comando "dict()":
'''
dados = dict()
dados = {}
'''
#Em dicionários o índice pode ser declarado literal, diferente das listas que seria "0, 1, 2, 3...".
#Dessa maneira abaixo:
dados = {'nome':'Pedro', 'idade':25}

#Em listas o "Pedro" teria o índice "0" e o "25" teria índice "1".
#Em dicionários é possível declarar o índice, nesse caso acima eu declarei "Pedro" como "nome" e "25" como "idade".
print(dados['nome'])
print(dados['idade'])

#Em dicionários o comando ".append()" não funciona. Para adicionar algo novo é declarado dessa maneira:
dados['sexo'] = 'M'
print(dados['sexo'])

#Para remover posso usar o comando "del" já visto anteriormente.
del dados['idade']
print(dados)

#Em dicionários é importante saber diferenciar "values(valores)", "keys(chaves)" e "items(itens)".
filme = {
    'titulo':'Star Wars',
    'ano':1977,
    'diretor':'George Lucas'
}

#Valores são o "conteúdo" do dicionário, nesse caso do dicionário "filme", os valores são "Star Wars", "1977" e "George Lucas".
print(filme.values())

#Keys são os índices, nesse caso do dicionário "filme", os keys são o "titulo", "ano" e "diretor".
print(filme.keys())

#Itens são a junção dos keys e dos valores, no caso do dicionário "filme" os itens são "titulo, Star Wars", "ano, 1977" e "diretor, George Lucas".
print(filme.items())

#Pode ser usado um "for" para o "items".
for k, v in filme.items():
    print(f"O {k} é {v}")

#Tuplas, listas e dicionários podem ser misturados, nesse caso abaixo eu tenho 3 dicionários dentro de uma lista.
locadora = [{'titulo':'Star Wars', 'ano':1977, 'diretor':'George Lucas'},
            {'titulo':'Avengers', 'ano':2012, 'diretor':'Joss Whedon'},
            {'titulo':'Matrix', 'ano':1999, 'diretor':'Wachowski'}]
print(locadora[0]['ano']) #Aqui o "0" representa o primeiro filme sendo"Star Wars". "ano" representa o ano do filme, no caso "1977".
print(locadora[2]['titulo']) #Aqui o "2" representa o último filme sendo o "Matrix". "titulo" representa o ano do filme sendo "1999".
