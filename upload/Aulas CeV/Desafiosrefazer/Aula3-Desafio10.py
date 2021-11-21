#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
celsius = float(input("Valor em graus Celsius: "))
fahrenheit = (celsius * 9 / 5) + 32
print(f"{celsius:.2f}°C são {fahrenheit:.2f}°F")