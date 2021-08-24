# Faça um algoritmo que leia o salário de um funcionário 
# e mostre seu novo salário, com 15% de aumento. 

salario = float(input('\nSalário do funcionário: R$ '))
porcento = int(input('Quantos porcento% de aumento? '))
aumento = (salario*porcento/100)
novo = salario + aumento
print(f'O funcionário que ganhava R$ {salario:.2f}, teve um aumento de R$ {aumento:.2f} com {porcento}% na promoção.')
print(f'Portanto, o novo salário do funcionário será de R$ {novo:.2f}!\n')