#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la. 
#Sabendo que cada litro de tinta, pinta uma área de 2 metros quadrados.
largura=float(input("Digite a largura da parede em metros: "))
altura=float(input("Digite a altura da parede em metros: "))
m2=largura*altura
tinta=m2/2
print("Sua parede tem {} metros quadrados.\nEntão você precisa de {} litros de tinta para pintar a parede inteira.".format(m2,tinta))