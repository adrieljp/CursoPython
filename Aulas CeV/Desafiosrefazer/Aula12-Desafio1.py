#Crie um programa que tenha uma TUPLA totalmente preenchida com uma contagem por extenso, de ZERO até VINTE.
#Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por EXTENSO.
numeros = ("zero", "um", "dois", "três", "quatro",
"cinco", "seis", "sete", "oito", "nove",
"dez", "onze", "doze", "treze", "quatorze",
"quinze", "dezesseis", "dezessete", "dezoito",
"dezenove", "vinte")
while True:
    num = int(input("Digite um número inteiro de 0 a 20: "))
    if 0 <= num <= 20:
        break
    print("Tente novamente. ", end='')
print(f"Você digitou o número {numeros[num]}")