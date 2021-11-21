'''
Em Python as variáveis compostas podem ser começadas de 3 maneiras, com "()" "[]" ou "{}".
() seria uma tupla.
[] seria uma lista.
{} seria um dicionário.
Detalhe que no Python novo não é preciso dos ().
Todo o código abaixo é puro fatiamento de strings.
'''
#lanche = 'Hambúrguer'
#lanche = 'Suco'
#print(lanche)


lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
print(lanche)

#Fatiamento de strings em uso abaixo.
print('////////////////////////////////////////////////////')

print(lanche[0]) or print(lanche[1]) or print(lanche[2]) or print(lanche[3])

print('////////////////////////////////////////////////////')

print(lanche[-4]) or print(lanche[-3]) or print(lanche[-2]) or print(lanche[-1]) or print(lanche[-3:])

print('////////////////////////////////////////////////////')

print(lanche[1:3]) or print(lanche[2:]) or print(lanche[:2])

print('////////////////////////////////////////////////////')
'''
Tuplas são IMUTÁVEIS. Ex:
lanche[1] = 'Refrigerante'
print(lanche[1])
Esse comando acima não irá funcionar.
'''

#As duas formas abaixo estão corretas podendo utilizar as duas.
for comida in lanche:
    print(f'Comi {comida}')
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]}') #Dessa maneira irá executar a variável lanche, aparecendo o nome de cada item dentro da tupla.
print('Comi muito.')

######################################################################################################################################################################################

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}.') #Dessa maneira irá executar a variável lanche, aparecendo o nome de cada item dentro da tupla.
                                                             #E a variável "cont" irá mostrar a posição dos itens que estão dentro da tupla.
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}') #Essa maneira é a mesma coisa que a maneira de cima só que sem usar o range.

######################################################################################################################################################################################

#A forma abaixo irá executar apenas números e não as variáveis.
for cont in range(0, len(lanche)):
    print(cont) #Dessa maneira irá executar números, irá aparecer 0, 1, 2, 3.

######################################################################################################################################################################################

#Para colocar a tupla em ordem alfabética usamos o comando "sorted". Igual ao exemplo abaixo:
print(sorted(lanche)) #Lembrando que isso não muda a tupla, veja no exemplo abaixo.
print(lanche) #Os dois funcionam, a diferença é que um está em ordem e o outro está normal, como sua origem.

######################################################################################################################################################################################

#Podemos "somar" tuplas, por exemplo:
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b #Lembrando que se for "b + a" a ordem muda.
print(c) #Aqui ele nao irá somar os número dando um resultado final, "a" e "b" serão juntados e a saída será "2, 5, 4, 5, 8, 1, 2".
print(len(c)) #Podemos também mostrar o tamanho da tupla com o comando "len", por exemplo a tupla "c" tem 7 elementos.
print(c.count(5)) #Podemos contar quantas vezes aparece um determinado caracter ou número dentro da tupla, no caso desse "print" irá aparecer 2 pq há dois números 5 entre a + b.
print(c.index(8)) #Comando "index" mostra a posição do número/caracter escolhido no caso desse print, o número escolhido foi o "8" que está na posição 4.
print(c.index(5, 1)) #Nesse caso ele ignorará o primeiro "5" pq o número "1" depois da vírgula indica que deve começar a contar apartir da posição "1".

#Sabemos que uma tupla é IMUTÁVEL, porém ela pode ser deletada, veja o exemplo abaixo:
pessoa = ('Adriel', 16, 'Masculino', 105)
del(pessoa) #O comando "del" serve para deletar qualquer variável, sendo composta ou não, lembrando que não é possível deletar um item da tupla, apenas ela inteira.
print(pessoa)