#Defini uma função para somar.
def soma(a, b):
    s = a + b
    print(s)
soma(4, 5)
soma(8, 9)
soma(2, 1)
#Lembrando que "4, 5", "8, 9" e "2, 1" são os parâmetros, então caso eu tente fazer "soma(4)" por exemplo, irá dar erro pq está faltando um parâmetro.

#Posso também fazer dessa maneira:
soma(a=4, b=1)
#Ou então mudar a ordem
soma(b=4, a=1)
#Desde que os parâmetros estão especificados na def, a ordem pode ser da maneira que quiser.

#ATENCAO! ESTOU CRIANDO OUTRA DEF PARA NÃO INTERFERIR NA DE CIMA.
#É possível fazer uma def formatada:
def soma2(c, d):
    print(f"C = {c} e D = {d}")
    s = c + d
    print(f"A soma C + D = {s}")
soma2(8, 9) 
soma2(d=8, c=9) #Lembrando que pode trocar a ordem também.

#Caso eu queira usar assim "soma(8, 9, 1)", o Python não irá aceitar pois não tem um terceiro parâmetro, porém é possível fazer isso de outra maneira.
#Em Python é possível declarar assim "def soma(* num)"
#Dessa maneira estou informando o Python que irá ser passado parâmetros. Quantos? Eu não sei, o Python que se vire.
#Se for passado um parâmetro irá ser jogado dentro de "num", se for passado 10 irá ser jogado dentro de "num" e se for passado 10 mil irá ser jogado dentro de "num".
'''
def contador(* num):
    print(num)
contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)
'''
#Na maneira acima, o output será em tuplas, mas é possível fazer o seguinte:
'''
def contador(* num):
    for valor in num:
        print(f"{valor} ", end='')
contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)
'''

#É possível mostrar o tamanho também:
'''
def contador(* num):
    tamanho = len(num)
    print(f"Recebi os valores {num} e ao todo são {tamanho} números.")
contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)
'''