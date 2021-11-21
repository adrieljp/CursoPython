#FUNÇÕES!
#Em Python para declarar uma função usamos o comando "def":
def linha(): #Lembrando que o nome pode ser o que quiser, é como se fosse uma váriavel.
    print("-" * 30)

#Para chamar a função, fazemos dessa maneira:
linha()

#É usado para facilitar o uso, fazer rotinas!
#Nesse caso abaixo, poderia usar a função "linha()" ao invés de escrever "print("-" * 30)".
print("-" * 30)
print("SISTEMA DE ALUNOS")
print("-" * 30)
print("CADASTRO DE FUNCIONÁRIOS")
print("-" * 30)
print("ERRO DE SISTEMA")
print("-" * 30)

#É possível usar funções com parâmetros também podendo automatizar ainda mais.
#Veja abaixo:
def mensagem(msg):
    print("-" * 30)
    print(msg)
    print("-" * 30)
mensagem('SISTEMA DE ALUNOS')
mensagem('CADASTRO DE FUNCIONÁRIOS')
mensagem('ERRO DE SISTEMA')
#Dessa maneira acima, quando a função mensagem é chamada, a frase escrita dentro substitui o parâmetro.
#E dentro da função o parâmetro está sendo "printado", ou seja, o que foi digitado dentro de mensgem será printado na tela.