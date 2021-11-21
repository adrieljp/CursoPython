#Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido.
#Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
from utilidadescev import dado
num = dado.leiaint("Digite um número inteiro: ")
num2 = dado.leiafloat("Digite um número real: ")
print(f"O valor inteiro digitado foi {num} e o real foi {num2}")