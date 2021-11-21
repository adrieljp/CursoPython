'''
nome = input('Qual seu nome? ')

print("Olá {}, é um prazer te conhecer!".format(nome))
'''

nome = input("Qual seu nome? ").strip().title()
print(f"Olá {nome}, é um prazer te conhecer!")