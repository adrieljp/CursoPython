#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
#IMC abaixo de 18,5: Abaixo do Peso
#Entre 18,5 e 25: Peso Ideal
#25 até 30: Sobrepeso
#30 até 40: Obesidade
#Acima de 40: Obesidade Mórbida
peso = float(input("Digite seu peso em KG: "))
altura = float(input("Digite sua altura em metros: "))
imc = peso / (altura ** 2)
if imc < 18.5:
    print("Seu IMC é de {:.1f}.\nCUIDADO! Você está ABAIXO do PESO.".format(imc))
elif imc > 18.5 and imc < 25:
    print("Seu IMC é de {:.1f}.\nPARABÉNS! Você está no PESO IDEAL.".format(imc))
elif imc > 25 and imc < 30:
    print("Seu IMC é de {:.1f}.\nCUIDADO! Você está com SOBREPESO.".format(imc))
elif imc > 30 and imc < 40:
    print("Seu IMC é de {:.1f}.\nCUIDADO! Você está com OBESIDADE.".format(imc))
elif imc > 40:
    print("Seu IMC é de {:.1f}.\nCUIDADO! Você está com OBESIDADE MÓRBIDA.".format(imc))