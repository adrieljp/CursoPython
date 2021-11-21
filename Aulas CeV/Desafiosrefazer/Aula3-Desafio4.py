#Crie um programa que leia o valor em metros e exiba ele convetido em centímetros e milímetros.
metros = float(input("Digite um valor em metros: "))
cm = metros * 100
mm = metros * 1000
print(f"{metros} metros é igual a\n{cm} centímetros.\n{mm} milímetros.")