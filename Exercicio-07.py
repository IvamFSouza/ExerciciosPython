# Faça um programa que leia a largura e a altura de uma parede em metros. 
# Calcule a sua área e a quantidade de tinta necessária para pinta-la, 
# sabendo que cada litro de tinta, pinta uma área de 2m². 

largura = float(input('\nLargura da parede: '))
altura = float(input('Altura da parede: '))
area = largura * altura
print(f'Sua parede tem a dimensão de {largura} x {altura} e área de {area}m²\n')