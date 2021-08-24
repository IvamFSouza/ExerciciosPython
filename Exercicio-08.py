# Faça um algoritmo que leia o preço de um produto e 
# mostre seu novo preço, com 5% de desconto.

preço = float(input('\nDigite o preço do produto: R$ '))
porcento = int(input('Digite o desconto: ')) # Será possível fixar o símbolo '%' no final deste input, para quando digitar ele fique atrás do número digitado?!
desconto = (preço*porcento/100)
print(f'O valor do produto é R$ {preço:.2f}, e terá R$ {desconto:.2f} de desconto com {porcento}%!\n')
novo = preço - desconto
print(f'Portanto, você pagará R$ {novo:.2f} no produto!\n')