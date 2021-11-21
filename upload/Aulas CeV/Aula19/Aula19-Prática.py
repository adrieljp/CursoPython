#Para o tratamento de erros (exceções), temos os comandos "try", "except", "else" e "finally".
#Try: O comando "try" irá tentar fazer a operação.
#Except: O "except" será o erro.
#Else: O "else" será o acerto.
#Finally: O "finally" será o acerto ou o erro, irá executar dando certo ou errado.
#Os comandos "else" e "finally" são opcionais, nem sempre serão usados.
#Veja alguns exemplos abaixo:
'''
a = int(input("Numerador: "))
b = int(input("Denominador: "))
r = a / b
print(f"O resultado é {r}")
'''

#Não tem nada de errado no programa acima, porém tem algumas limitações como:
#Caso no "denominador" o usuário digite "0" irá dar um erro (exceção) pq um número não se pode dividir por 0.
#Então pode ser usado dessa maneira:

'''
try:
    a = int(input("Numerador: "))
    b = int(input("Denominador: "))
    r = a / b
except:
    print("Tivemos um problema :(")
print(f"O resultado é {r:.2f}")
'''

#Nesse programa acima caso tenha um problema, irá aparecer na tela o "except" e também a exceção.
#Para não aparecer a exceção podemos usar o "else".

'''
try:
    a = int(input("Numerador: "))
    b = int(input("Denominador: "))
    r = a / b
except:
    print("Tivemos um problema :(")
else: 
    print(f"O resultado é {r:.2f}")
''' 

#Nesse caso acima, está se informado para o compilador o seguinte:
#"Tente essa operação, se tiver problema, o "except" irá aparecer, caso esteja tudo certo, mostre o "else"."

#E podemos usar o "finally" que irá ser executado independente se der erro ou não.

'''
try:
    a = int(input("Numerador: "))
    b = int(input("Denominador: "))
    r = a / b
except:
    print("Tivemos um problema :(")
else:
    print(f"O resultado é {r:.2f}")
finally:
    print("Volte sempre! Muito obrigado!")
'''

#Caso você queira mostrar o erro ao usuário ao invés de dizer que teve um problema que é uma coisa muito genérica.
#Você pode usar o comando "Exception".
'''
try:
    a = int(input("Numerador: "))
    b = int(input("Denominador: "))
    r = a / b
except Exception as erro:
    print(f"O problema encontrado foi {erro.__class__}")
else:
    print(f"O resultado foi {r:.2f}")
finally:
    print("Volte sempre! Muito obrigado!")
'''

#Um "try" pode ter vários "except", como se fosse um "if" e "elif".
try:
    a = int(input("Numerador: "))
    b = int(input("Denominador: "))
    r = a / b
except (ValueError, TypeError):
    print("Tivemos um problema com os tipos de dados digitados.")
except ZeroDivisionError:
    print("Não é possível dividir um número por zero.")
except KeyboardInterrupt:
    print("O usuário preferiu não informar os dados.")
else:
    print(f"O resultado foi {r:.2f}")
finally:
    print("Volte sempre! Muito obrigado!")