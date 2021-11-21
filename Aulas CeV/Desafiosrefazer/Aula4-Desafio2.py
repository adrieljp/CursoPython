#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
#Calcule e mostre o comprimento da hipotenusa.
oposto = float(input("Informe o cateto oposto: "))
adjacente = float(input("Informe o cateto adjacente: "))
hipotenusa = (oposto * oposto) + (adjacente * adjacente)
print(f"A partir do cateto oposto {oposto:.2f} e do cateto adjacente {adjacente:.2f}, podemos concluir que a hipotenusa é {hipotenusa:.2f}.")