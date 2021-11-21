#Crie um programa que leia duas notas de um aluno e calcule a média mostrando uma mensagem final, de acordo com a média atingida:
#Se a média for abaixo de 5.0: REPROVADO
#Se a média for entre 5.0 e 6.9: RECUPERAÇÃO
#Se a média for 7.0 ou acima: APROVADO
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2) / 2
if media < 5:
    print("A sua média foi {:.1f} e você foi REPROVADO!".format(media))
elif media >= 5 and media <= 6.9:
    print("A sua média foi {:.1f} e você está em RECUPERAÇÃO.".format(media))
else:
    print("A sua média foi {:.1f} e você foi APROVADO.".format(media))