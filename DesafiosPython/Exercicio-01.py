# Fazer com que o interepretador leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.

n = int(input('Digite um valor: '))
a = n  - 1
s = n + 1
print('\nAnalisando o valor {}, seu antecessor é {} e o sucessor é {}\n'.format(n, a, s))