# Crie um programa que leia o nome completo de uma pessoa e mostre:
# · O nome com todas as letras maiúsculas;
# · O nome com todas as letras minúsculas;
# · Quantas letras ao todo (sem considerar espaços);
# · Quantas letras tem o primeiro nome.

nome = str(input('\nDigite seu nome completo: ')).strip()
print('+'*22)
print('Analisando seu nome...')
print('+'*22)
print(f'Seu nome com letras maiúsculas: {nome.upper()}')
print(f'Seu nome com letras minúsculas: {nome.lower()}')
print(f'O seu nome {nome}, tem',len(nome) - nome.count(' '),'letras.')
#print(f'Seu primeiro nome tem: {nome} letras.',(nome.find(' ')))
separa = nome.split()
print(f'Seu primeiro nome é {separa[0]} e tem',len(separa[0]),'letras' )
print('\n')