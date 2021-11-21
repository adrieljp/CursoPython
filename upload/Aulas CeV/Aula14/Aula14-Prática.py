galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
for p in galera:
    print(p)
    print(p[0])
    print(p[1])
    print(f'{p[0]} tem {p[1]} anos.')

##########################################################################################

galera2 = list()
dado = list()
totmai = totmen = 0
for c in range(1, 4):
    dado.append(input("Nome: "))
    dado.append(int(input("Idade: ")))
    galera2.append(dado[:])
    dado.clear()
for p in galera2:
    print(f'{p[0]} tem {p[1]} anos.')
    if p[1] >= 18:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmen += 1
print(f"No total tivemos {totmai} pessoas maiores de idade e {totmen} pessoas menores de idade.")