# faça um programa que leia o comprimento do cateto oposto e do cateto adjacente
# de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.

''' modo sem importação
co = float(input('\nComprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print(f'A hipotenusa vai medir {hi:.2f}.')'''

# com modo de importação
from math import hypot
co = float(input('\nComprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = hypot(co, ca)
print(f'A hipotenusa vai medir {hi:.2f}.')