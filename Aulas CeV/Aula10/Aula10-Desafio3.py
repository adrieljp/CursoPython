#Crie um programa que leia dois valores e mostre um menu na tela:
#[ 1 ] somar
#[ 2 ] multiplicar
#[ 3 ] maior
#[ 4 ] novos números
#[ 5 ] sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso.
from time import sleep
num1 = float(input("Digite um valor: "))
num2 = float(input("Digite outro valor: "))
op = True
while op:
    print("-=-" * 30)
    print("[ 1 ] Somar\n[ 2 ] Multiplicar\n[ 3 ] Mostrar o maior entre os dois valores digitados\n[ 4 ] Novos números\n[ 5 ] Sair do programa")
    op = int(input("Escolha sua opção: "))
    if op == 1:
        resultado = num1 + num2
        print(f"O resultado entre {num1} + {num2} é {resultado}.")
        sleep(3)
    elif op == 2:
        resultado = num1 * num2
        print(f"O resultado entre {num1} x {num2} é {resultado}.")
        sleep(3)
    elif op == 3:
        if num1 > num2:
            print(f"Entre {num1} e {num2} o maior é o {num1}")
            sleep(3)
        else:
            print(f"Entre {num1} e {num2} o maior é o {num2}")
            sleep(3)
    elif op == 4:
        num1 = float(input("Digite um valor: "))
        num2 = float(input("Digite outro valor: "))
    elif op == 5:
        sleep(0.5)
        print("Finalizando...")
        sleep(1.5)
        print("Fim do programa. Obrigado por usar e volte sempre!\n")
        op = False
    else:
        print("OPÇÃO INVÁLIDA. TENTE NOVAMENTE")