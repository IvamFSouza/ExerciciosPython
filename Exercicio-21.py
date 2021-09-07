# Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome.

nome = str(input('\nQual é o seu nome completo? ')).strip()
#print('Seu nome tem Silva? {}.'.format('SILVA' in nome.upper()))
print(f'Seu nome tem Silva? {"SILVA" in nome.upper()}')
