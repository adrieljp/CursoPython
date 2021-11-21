#Crie um programa que vai gerar CINCO NÚMEROS ALEATÓRIOS e colocar em uma TUPLA.
#Depois disso, mostre a listagem de números gerados e também indique o MENOR e o MAIOR valor que estão na tupla.
from random import randint
nums = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f"Números gerados: ", end='')
for n in nums:
    print(n, end=' ')
#Nesse exercício irei usar dois comandos novos, os comandos "max" e "min" eles mostram o maior e menor valor.
print(f"\nO maior valor sorteado foi {max(nums)}")
print(f"O menor valor sorteado foi {min(nums)}")