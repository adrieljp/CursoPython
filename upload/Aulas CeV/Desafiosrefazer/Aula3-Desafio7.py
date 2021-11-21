#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la. 
#Sabendo que cada litro de tinta, pinta uma área de 2 metros quadrados.
largura = float(input("Largura da parede em metros: "))
altura = float(input("Altura da parede em metros: "))
area = largura * altura
tinta = area / 2
print(f"Largura digitada: {largura:.2f}")
print(f"Altura digitada: {altura:.2f}")
print(f"Área da parede em metros quadrados: {area:.2f}")
print(f"Litros de tinta necessários para pintar a parede toda: {tinta:.2f}")