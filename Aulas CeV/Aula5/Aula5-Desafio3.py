# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".
cidade=input("Digite o nome da sua cidade: ").strip().upper()
print(cidade[:5] == "SANTO")
