# Fazer com que o interpretador leia duas notas de um aluno, calcule e mostre a sua média.

n1 = float(input('\nDigite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
print('\nA primeira nota é: {:.1f}.'.format(n1))
print('A segunda nota é: {:.1f}.'.format(n2))
print('Portanto, sua média é: {:.1f}.\n'.format(media))