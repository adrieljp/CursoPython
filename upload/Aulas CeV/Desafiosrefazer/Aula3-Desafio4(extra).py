#Crie um programa que leia o valor em metros e exiba ele convetido em quilômetros, hectometros, decâmetros, decímetros, centímetros e milímetros.
metros = float(input("Digite um valor em metros: "))
km = metros / 1000
hm = metros / 100
dam = metros / 10
dm = metros * 10
cm = metros * 100
mm = metros * 1000
print(f"{metros:.2f} metros são:\n{km:.2f} km\n{hm:.2f} hm\n{dam:.2f} dam\n{dm:.2f} dm\n{cm:.2f} cm\n{mm:.2f} mm.")