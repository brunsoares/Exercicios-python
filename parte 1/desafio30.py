#pegando valor
numUsu = int(input('Digite um número: '))

if numUsu % 2 == 0:
    print('Seu número é {}, e ele é par'.format(numUsu))
else:
    print('Seu número é {}, e ele é impar'.format(numUsu))

'''
    Primeiro o usuário vai digitar um valor armazenado em numUsu
    Na verificação, se o na divisão real do numUsu por 2 RESTAR (%) 0, significa que o número é par
    Assim será printado o número mostrando que ele é par
    Caso não caia no if, o else manda o número e mostra que ele é impar
'''
