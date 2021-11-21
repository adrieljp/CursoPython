#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
celsius=float(input("Digite um valor em graus celsius: "))
fah=(celsius * 9/5)+32
print("{:.1f} graus celsius é {:.1f} graus fahrenheit.".format(celsius, fah))