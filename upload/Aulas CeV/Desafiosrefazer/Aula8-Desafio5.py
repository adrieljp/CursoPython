#Crie um programa que leia duas notas de um aluno e calcule a média mostrando uma mensagem final, de acordo com a média atingida:
#Se a média for abaixo de 5.0: REPROVADO
#Se a média for entre 5.0 e 6.9: RECUPERAÇÃO
#Se a média for 7.0 ou acima: APROVADO
nota1 = float(input("Primeira nota: "))
nota2 = float(input("Segunda nota: "))
media = (nota1 + nota2) / 2
if media < 5:
    print(f"Suas notas foram {nota1:.1f}, {nota2:.1f} e a média foi {media:.1f}")
    print("REPROVADO!")
elif media >= 5 and media <= 6.9:
    print(f"Suas notas foram {nota1:.1f}, {nota2:.1f} e a média foi {media:.1f}")
    print("RECUPERAÇÃO!")
else:
    print(f"Suas notas foram {nota1:.1f}, {nota2:.1f} e a média foi {media:.1f}")
    print("APROVADO!")