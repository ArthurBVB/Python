# + adição - subtração * multiplicação / divisão ** potencia
#divisão inteira // e % resto da divisão

nome = input('qual é o seu nome? ')

print('Prazer em te conhecer {:=^20}!'.format(nome))

n1= int(input('Um valor: '))
n2= int(input('Outro valor: '))

print('A Soma vale {}'.format(n1+n2), end=' ')
print('A multiplicação vale {}\n a divisão é {:.3f} a divisão inteira é {} e a portencia é {}'.format(n1*n2,n1/n2,n1//n2,n1**n2))
