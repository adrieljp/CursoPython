# OPERAÇÕES ARITMÉTICAS:
# Ordem de precedência das operações aritméticas.
# 1 - ()                    () = parenteses
# 2 - **                    ** = exponenciação
# 3 - *, /, //, %           * = Multiplicação. / = Divisão. // = Divisão inteira. % = Resto da divisão.
# 4 - +, -                  + = Soma. - = Subtração.


#fazer uma calculadora que mostre: somar, subtrair, multiplicar, dividir, divisao inteira, resto da divisao e exponenciação.
n1=int(input("Digite o primeiro valor: "))
n2=int(input("Digite o segundo valor: "))
s=n1+n2
sub=n1-n2
mult=n1*n2
div=n1/n2
divint=n1//n2
restodiv=n1%n2
expo=n1**n2
print("A soma dos valores é {:.2f}\nA subtração é {:.2f}\nA multiplicação é {:.2f}\nA divisão é {:.2f}\nA divisão inteira é {:.2f}\nO resto da divisão é {:.2f}\nA exponenciação é {}.".format(s, sub, mult, div, divint, restodiv, expo))