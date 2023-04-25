dias= int (input('Quantos dias voce ficou com o carro? '))
km=float (input('Quanos Kms foram rodados? '))

print('O valor a ser pago de aluguel total sera {:2} reais, sendo {:2} reais pelos {} dias e {:2}reais pelos {} KMs'.format(60*dias+0.15*km,60*dias,dias,km*0.15,km))