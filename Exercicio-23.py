# Faça um programa que leia o nome compelto de uma pessoa,
# mostrando em seguida o primeiro e o último nome separadamente.
# Ex.: Ana Maria de Souza
#      Primeiro nome: Ana
#      Último nome: Souza

n = str(input('\nDigite seu nome completo: ')).strip()
nome = n.split()
print('\nMuito prazer em te conhecer!')
print(f'Seu primeiro nome é {nome[0]}')
print(f'Seu último nome é {nome[len(nome)-1]}\n')