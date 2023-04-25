preco=float (input('Digite o preço de um produto= '))
desconto= float(input('Digite quantos por cento de desconto em liquidação= '))
cdesc=desconto/100*preco
precofinal=preco-cdesc

print('O preço do produto é {:.2f} Reais o valor do desconto sera {:.2f} Reais e o valor final da peça com desconto é {:.2f} Reais'.format(preco,cdesc,precofinal))