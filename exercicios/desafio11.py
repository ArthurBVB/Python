a= float(input('Qual é a altura em metros dessa parede?= '))
b= float(input ('Qual  é a largura em metros dessa parede?= '))
ar= a*b
tinta= 2
print('sabendo que cada litro de tinta pinta {:.2f} Metros quadrados. Sera necessario {:.2f} litros de tinta para pintar essa parede ou seja {:.2f} latas '.format(tinta,ar/tinta,ar/tinta/2))