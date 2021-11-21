#Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
#O primeiro que indique o número a calcular .
#O outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.
def fatorial(num, show=False):
    f = 1
    for c in range(num, 0, -1):
        if show == True:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f
print(fatorial(5))