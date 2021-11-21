#Listas (PARTE 1)
lanche = ['Hambúrguer', 'Suco', 'Pizza', 'Pudim']
print(lanche)

#Diferente das tuplas, as listas são mutáveis então se eu quiser trocar o "Pudim" por "Picolé" por exemplo, eu posso fazer isso.

lanche[3] = 'Picolé'
print(lanche)

#É possível também adicionar mais itens com o comando ".append", esse comando irá adicionar no final da lista.

lanche.append('Cookie')
print(lanche)

#Também é possível adicionar mais itens em outra posição a não ser a última, fazemos isso com o comando ".insert".

lanche.insert(0, 'Cachorro Quente') #O número "0" indica a posição que o item será adicionado.
print(lanche)

#Podemos remover algum item da lista de 3 maneiras, com o comando "del" com o comando ".pop()" ou com o comando ".remove".
del lanche[3]
print(lanche)

######################################################################################################################################################################################

lanche.pop(0) #Se o comando pop for usado dessa maneira "lanche.pop()", o último elemento da lista será removio, lembrando que apenas o comando ".pop" faz essa função.
print(lanche)

######################################################################################################################################################################################

lanche.remove('Cookie')
print(lanche)

######################################################################################################################################################################################

#Uma lista também pode ser declarada com a função "list", por exemplo caso eu queira fazer uma contagem eu posso fazer da seguinte forma:
valores = list(range(4, 11)) #A contagem de "4" até "10" foi armazenada na variável "valores"
print(valores)

#Caso uma lista com números aleatórios for criada, posso usar o comando ".sort()" para ordenar em ordem crescente, por exemplo:
valores = [8, 2, 5, 4, 9, 3, 0]
print(valores)
valores.sort()
print(valores)

#Caso eu queira ordenar em ordem decrescente, irei definir um parametro para o comando "sort", ficaria assim: ".sort(reverse=True)"
valores.sort(reverse=True)
print(valores)

######################################################################################################################################################################################

#O comando "len" pode ser usado também e é útil para fazer laços.
print(len(valores))