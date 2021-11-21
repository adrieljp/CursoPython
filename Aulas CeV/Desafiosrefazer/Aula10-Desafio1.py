#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. 
#Caso esteja errado, peça a digitação novamente até ter um valor correto.
while sexo not in "MF":
    sexo = input("Informe seu sexo [M/F]: ").upper().strip()
    if sexo == "M":
        print("Sexo M registrado com sucesso.")
    elif sexo == "F":
        print("Sexo F registrado com sucesso.")
    else:
        print("DADOS INVÁLIDOS. Por favor tente novamente.")
