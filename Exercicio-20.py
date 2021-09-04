# Crie um programa que leia o nome de uma cidade e que mostre 'True'
# se ela começa com "Santo" ou 'False' se não.

cidade = str(input('\nEm que cidade você nasceu? ')).strip()
print(cidade[:5].upper() == 'SANTO')
print('\n')