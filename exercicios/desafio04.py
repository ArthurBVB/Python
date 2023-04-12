n = input('Digite algo: ')
print ('O tipo primitivo desse valor é ', type(n))
print('voce digitou algo numerico? {}'.format( n.isnumeric()))
print('voce digitou uma palavra? {}'.format( n.isalpha()))
print('voce digitou uma palavra ou numero? {}'.format( n.isalnum()))
print('voce digitou somente espaço? {}'.format( n.isspace()))
print('Esta em letra maiuscula? {}'.format( n.isupper()))
print('é um titulo? primeira letra maiuscula {}'.format( n.istitle()))



