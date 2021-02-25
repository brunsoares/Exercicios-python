#preço do produto
prod = float(input('Qual o valor do produto desejado: '))
desc = prod * 0.05  #0.05 desconto de 5%
precoDesc = prod - desc
print('O produto desejado custa R${:.2f}, porém com o nosso desconto de 5% fica R${:.2f}'.format(prod, precoDesc))

'''
    O usuário digita um valor float que será armazenado em prod
    O desc irá calcular o desconto sobre o valor (desconto de 5%)
    O precoDesc vai descontar do preço atual o desconto
    E depois será printado com uma leve "formatação" em real
'''
