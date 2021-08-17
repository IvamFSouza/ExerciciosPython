# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

medida = float(input('Digite a distância em metros: '))
mm = medida * 1000
cm = medida * 100
dm = medida * 10
dam = medida / 10
hm = medida / 100
km = medida / 1000
print('\nA medida de {} m corresponde a: \n{:.0f} mm \n{:.0f} cm \n{:.0f} dm \n{} dam \n{} hm \n{} km'.format(medida, mm, cm, dm, dam, hm, km))