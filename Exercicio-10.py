# Escreva um programa que converta uma temperatura digitada em °C e converta para °F. 

c = float(input('\nInforme a temperatura em °C: '))
f = (9*c)/5 + 32
print(f'A temperatura de {c:.0f}°C (Celsius) corresponde a {f:.0f}°F (Fahrenheit)!\n')