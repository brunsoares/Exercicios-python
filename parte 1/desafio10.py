#valor na carteira da pessoa
print('Por favor coloque no modelo americano (0.00)')
real = float(input('Quantos reais você tem no bolso agora: R$'))
dol = real / 5.42
print('Com R${:.2f} você consegue comprar US${:.2f}, triste né'.format(real, dol))

'''
    O programa pede ao usuário para digitar um valor que será armazenado na variavel real
    Depois MANUALMENTE a variavel dol converte o reais pela cotação atual do dolár (24/02/2021)
    Depois printada no print usando duas casas depois da virgula
'''
