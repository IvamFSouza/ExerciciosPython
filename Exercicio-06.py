# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar:
# Considerando:
# USD 1.00 = R$ 5.40

real = float(input('\nQuanto dinheiro você tem na carteira? \nR$ '))
dolar = real / 5.40
print('Com R$ {:.2f} você pode comprar USD {:.2f}\n'.format(real, dolar))