#Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
#O programa será interrompido quando o número solicitado for negativo.
while True:
    n = int(input("Quer ver a tabuada de qual valor? "))
    print("-" * 40)
    if n < 0:
        break
    for tabuada in range(1, 11):
        total = n * tabuada
        print(f"{n} x {tabuada} = {total}")
    print("-" * 40)
print("Obrigado por ter usado o programa de tabuada. Volte sempre!")