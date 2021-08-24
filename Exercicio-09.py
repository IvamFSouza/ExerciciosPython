# Faça um algoritmo que leia o salário de um funcionário 
# e mostre seu novo salário, com 15% de aumento. 

salario = float(input('\nSalário do funcionário: R$'))
aumento = salario + (salario*15/100)
print(f'O funcionário que ganhava R$ {salario:.2f}, teve um aumento de 15% e passou a receber R$ {aumento:.2f}.\n')