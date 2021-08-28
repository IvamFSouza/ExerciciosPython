# Faça um programa que leia um ângulo qualquer e mostre na tela 
# o valor do Seno, Cosseno e Tangente desse ângulo.

import math

angulo = float(input('\nDigite o ângulo que você deseja: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print(f'O ângulo de {angulo:.0f}° tem o Seno de {seno:.2f}.')
print(f'O ângulo de {angulo:.0f}° tem o Cosseno de {cosseno:.2f}.')
print(f'O ângulo de {angulo:.0f}° tem a Tangente de {tangente:.2f}.\n')