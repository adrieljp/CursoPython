#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.
a=input("Digite algo: ")
print("Qual o tipo primitivo? {}".format(type(a)))
print("É alfabético? {}".format(a.isalpha()))
print("É alfanumérico? {}".format(a.isalnum()))
print("É numérico? {}".format(a.isnumeric()))
print("É digíto? {}".format(a.isdigit()))
print("Tem espaços? {}".format(a.isspace()))
print("É capitalizado? {}".format(a.istitle()))
print("É letras maiúsculas? {}".format(a.isupper()))
print("É letras minúsculas? {}".format(a.islower()))