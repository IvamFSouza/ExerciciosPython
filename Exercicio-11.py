# Escreva um programa que pergunte a quantidade de km percorridos 
# por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0.15 por km rodado.

km = float(input('\nQuantos km rodados? '))
dias = int(input('Quantos dias alugados? '))
valor_km = km * 0.15
valor_dias = dias * 60
total = valor_km + valor_dias
print(f'\nForam percorridos {km:.0f}km ao custo de R$0.15 por km, o custo é de R${valor_km:.2f}.')
print(f'O carro ficou alugado por {dias:.0f} dias, ao custo de R$ 60 por dia, custará R$ {valor_dias:.2f}.')
print(f'\nO valor total a ser pago é de R$ {total:.2f}!\n')