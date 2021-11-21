#Crie um programa que leia o valor em metros e exiba ele convetido em quilômetros, hectometros, decâmetros, decímetros, centímetros e milímetros.
metros=float(input("Digite um valor em metros: "))
km=metros/1000
hm=metros/100
dam=metros/10
dm=metros*10
cm=metros*100
mm=metros*1000
print("{:.2f} metros são:\n{:.2f} km\n{:.2f} hm\n{:.2f} dam\n{:.2f} dm\n{:.2f} cm\n{:.2f} mm.".format(metros, km, hm, dam, dm, cm, mm))