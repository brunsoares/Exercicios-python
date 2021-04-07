#Int
try:
    num = int(input('Digite um valor int: '))

    def leiaint(n):
        return n
except Exception as error:
    print('Número invalido, tente novamente...')
    print(f'Invalido pois deu esse erro: {error.__class__}')
else:
    print(f'O valor int foi = {leiaint(num)}')

#Float
try:
    flo = float(input('Digite um valor float: '))
    def leiaflo(f):
        return f
except Exception as error:
    print('Número invalido, tente novamente...')
    print(f'Invalido pois deu esse erro: {error.__class__}')
else:
    print(f'O valor float foi = {leiaflo(flo)}')

'''
    Primeiro programa para tratamento de erros
    Primeiro vamos tratar o erro de números int, então jogamos primeiro a estrutura try
    Que vai tentar executar esse código de interação com o usuário e criação da função
    Caso não consiga ele cai na except, isso é como, tente fazer isso, caso não consiga
    No except, usamos o Exception as error, para a variavel error receber valores de exception
    Assim podemos ver o erro, como é mostrado pelo, error.__class__ que mostra a classe do erro
    Caso contrario, ele consiga tentar com o try, o else vai mostrar o valor
    Isso vale para o primeiro (INT) e o segundo (FLOAT)
'''
