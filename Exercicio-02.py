# Criar um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

n = int(input('\nDigite um valor: '))
d = n * 2
t = n * 3
r = n ** (1/2)
print('\nO dobro de {} é {}.'.format(n, d))
print('O triplo de {} é {}.'.format(n, t))
print('A raiz quadrada de {} é {:.2f}.\n'.format(n, r))