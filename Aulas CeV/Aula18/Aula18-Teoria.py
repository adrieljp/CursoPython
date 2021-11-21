#                                                                        MODULARIZAÇÃO
#                                                                           MÓDULOS
#1. Surgiu no início da década de 60.
#2. Sistemas começaram a ficar cada vez maiores
#3. Com sistemas cada vez maiores, o foco era dividir esses sistemas, no caso dividir um programa muito grande.
#4. E também como foco, aumentar a legibilidade do código, como por exemplo para encontrar um erro.
#5. Ficando mais fácil de encontrar o erro consequentemente fica mais fácil fazer a manutenção do sistema.

'''
def fatorial(n):
    f = 1
    for c in range(1, n+1):
        f *= c
    return f


def dobro(n):
    return n * 2


def triplo(n):
    return n * 3


num = int(input("Digite um valor: "))
fat = fatorial(num)
print(f"O fatorial de {num} é {fat}")
print(f"O dobro de {num} é {dobro(num)}")
print(f"O triplo de {num} é {triplo(num)}")
'''
#Acima é um programa normal já conhecido, mas é possível modular esse programa.
#Nesse caso acima, a modularização do programa seria retirar coisas que ja sabemos que funciona para não atrapalhar.
#Iremos tirar as funções e colocar dentro de outro arquivo criado dentro dessa pasta.
#Para o programa funcionar sem as funções digitadas dentro desse arquivo, basta importar o outro arquivo, veja abaixo:
'''
from uteis import fatorial, dobro, triplo
num = int(input("Digite um valor: "))
fat = fatorial(num)
print(f"O fatorial de {num} é {fat}")
print(f"O dobro de {num} é {dobro(num)}")
print(f"O triplo de {num} é {triplo(num)}")
'''
#Assim como outro módulo, é possível usar o "from" ou apenas o "import" e importar o módulo inteiro
#Lembrando que se importar o módulo inteiro, tem que usar a referencia antes do método.
#Caso seja importado o módulo inteiro usar a referência: uteis.fatorial
#Caso não seja importado o módulo inteiro, não usar a referência: fatorial

#Vantagens da modularizção e módulos:
#1. Organização do código
#2. Facilidade na manutenção
#3. Ocultação do código detalhado
#4. Reutilização em outros projetos

#                                                                          PACOTES
#O objetivo dos módulos são para ajudar na manutenção, organização e etc. Mas os módulos tem uma limitação, e se eu tenho muuuuitas funções dentro de um módulo?
#Todo aquele objetivo de organização e ajuda na manutenção foi pro ralo.
#E é por isso que existem os pacotes, os pacotes são nada mais que vários módulos juntos em um só, dentro de um pacote pode-se separar por assuntos.
#Por exemplo, eu posso ter um assunto chamado "números" e dentro de "números" são várias funções que lidam com números .
#Ou então um assunto chamado "strings", que são várias funções que lidam com strings.
#Pacotes servem para organizar vários módulos, os módulos são separados por assuntos, facilitando tudo novamente.
#Como criar um pacote? Bom, para criar um módulo basta criar um arquivo .py e para criar um pacote, ao invés de criar um arquivo, crie uma pasta.
#Lembrando que dentro de um pacote, pode ter outros pacotes, ou seja, outras pastas.
#Ao criar um pacote, caso seja criado um módulo, nada muda ao importar.
#Porém se é criado um pacote dentro de outro pacote, o arquivo a se criar dentro do segundo pacote não é um arquivo normal como se fosse um módulo.
#O arquivo que terá que ser criado é chamado de "__init__.py" e esse arquivo será o módulo, todo o código que será digitado nele.
#Para importar um pacote dentro de outro pacote, no caso aqui seria "import uteis" ou então "from uteis import numeros".
#Ao importar "numeros", ele será a referência ao usar no código, ao invés de digitar "uteis.fatorial", será digitado "numeros.fatorial".
#Veja abaixo:
from uteis import numeros
num = int(input("Digite um valor: "))
fat = numeros.fatorial(num)
dobro = numeros.fatorial(num)
triplo = numeros.fatorial(num)
print(f"O fatorial de {num} é {fat}")
print(f"O dobro de {num} é {dobro}")
print(f"O triplo de {num} é {triplo}")