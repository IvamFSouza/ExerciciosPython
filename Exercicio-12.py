# Crie um programa que leia um número qualquer pelo teclado 
# e mostre na tela a sua porção inteira. 
# Ex.: Digite um valor: 6127
#      O valor 6127 tem o número 6 como porção inteira.

# (Funciona com o módulo floor também!)

from math import trunc
num = float(input('\nDigite um valor: '))
print(f'O valor digitado foi {num:.0f} e a sua porção inteira é {trunc(num)}\n')