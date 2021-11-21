#FUNÇÕES(PARTE 2)
#                                                                 INTERACTIVE HELP
#Em Python temos um manual chamado de Interactive Help, ele explica o que um comando faz, podemos usar no console do python a função "help()".
#Ou então, dentro do codigo, podemos usar "help()" e dentro dos () digitar o comando que queremos ver o manual de instrução.
help(print)

#É possível usar o manual com o "__doc__" também (particularmente, prefiro o "help()")
print(input.__doc__)

#                                                                    DOCSTRINGS
#Docstrings serve basicamente como um "help()" para funções criadas por usuários, por exemplo:
def linha():
    '''
    Essa função foi criada para adicionar linhas.
    Função criada por ADJP.
    '''
    print("-=" * 20)
linha()
help(linha)
#Tudo o que está dentro das aspas, aparecerá como o manual de instrução!

#                                                               PARÂMETROS OPCIONAIS
#Em uma função de somar por exemplo, se ela recebe 3 parâmetros mas na chamada é dado apenas 2 parâmetros, o que fazer?
'''
def somar(a, b, c):
    s = a + b + c
    print(f"A soma vale {s}.")
somar(3, 2, 5)
somar(8, 4)
'''
#Nessa maneira acima daria erro pois o C não está recebendo um valor, como resolver isso?
#Para resolver isso, fazemos do C um parâmetro opcional dessa maneira:
def somar(a, b, c=0):
    s = a + b + c
    print(f"A soma vale {s}.")
somar(3, 2, 5)
somar(8, 4)
#Dessa maneira acima o C só irá valer alguma coisa caso seja dado um parâmetro para ele na chamada.
#Lembrando que em Python nada impede de atribuir 0 para todos os parâmetros.

#                                                                 ESCOPO DE VARIÁVEIS
#Existem dois tipos de vriáveis, as variáveis globais e as variáveis locais.
#As globais são as que são declaradas fora das identações e funcionam em todo o programa incluindo dentro de uma função.
#As locais são as que são declaradas dentro de uma identação e funcionam apenas dentro daquela função por exemplo.
#Veja abaixo um exemplo:
def teste(b):
    a = 8 #Variável local que valerá 8 apenas na função teste.
    b += 4
    c = 2
    print(f"A dentro vale {a}")
    print(f"B dentro vale {b}")
    print(f"C dentro vale {c}")
#Programa Principal
a = 5 #Variável global que funcionará fora da função teste.
teste(a)
print(f"A fora vale {a}")

#Mas caso você queira tornar uma variável local em global, use o comando "global", veja abaixo:
def teste2(b):
    global a
    a = 8 
    b += 4
    c = 2
    print(f"A dentro vale {a}")
    print(f"B dentro vale {b}")
    print(f"C dentro vale {c}")
#Programa Principal
a = 5 #Essa variável receberá o valor "8" pois a variável "A" declarada dentro da função se tornou global e substituiu o "5".
teste2(a)
print(f"A fora vale {a}")

#                                                                 RETORNANDO VALORES
#Para retornar um valor usamos o comando "return", esse método serve para personalização, veja abaixo um exemplo:
def somar(a=0, b=0, c=0):
    s = a + b + c
    print(f"A soma vale {s}")
somar(3, 2, 7)
somar(7, 6)
somar(6)
#Nesse caso acima o output seria de "A soma vale {s}" 3 vezes
#Caso eu queira fazer o output "Os resultados foram: {} {} {}", eu não iria conseguir dessa maneira pois não é possível
#E então com essa limitação, usamos o comando "return", veja abaixo:
def somar2(a=0, b=0, c=0):
    s = a + b + c
    return s
soma1 = somar2(3, 2, 7)
soma2 = somar2(7, 6)
soma3 = somar2(6)
print(f"Os resultados foram {soma1}, {soma2} e {soma3}")
#Dessa maneira acima, o "return" retorna o valor para as variáveis tirando a limitação de repetição.