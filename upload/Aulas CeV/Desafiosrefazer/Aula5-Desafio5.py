# Faça um programa que leia um frase pelo teclado e mostre:
# Quantas vezes aparece a letra "A".
# Em que posição ela aparece a primeira vez.
# Em que posição ela aparece a ultima vez.
frase=input("Digite uma frase: ").strip().upper()
print("A letra A aparece {} vezes.".format(frase.count("A")))
print("A letra A aparece pela primeira vez na posição {}.".format(frase.find("A")+1))
print("A letra A aparece pela ultima vez na posição {}.".format(frase.rfind("A")+1))
