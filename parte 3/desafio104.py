#func com while para aceitar apenas um tipo de valor
def leiaInt(num):
    while not num.isnumeric():
        print('\033[31mDigite um valor númerico valido\033[m')
        num = input('Digite um valor: ')

    return num

n = leiaInt(input('Digite um valor: '))
print(f'Seu número é {n}')

'''
    Função para apenas ler um tipo de valor, sendo número int apenas, essa função será usada bastante mais pra frente
    Primeiro criamos a função leiaInt() que recebe um parametro
    Dentro usamos o loop infinito que enquanto o parametro não for númerico, não sai do loop
    Dentro do loop é informado um print de número invalido, em seguida pede novamente oo número
    Por fim é retornado o parametro
    Fora da função temos a variavel n que chama a função leiaInt() que recebe como parametro a interação do usuário
    Por fim é mostrado o resultado
'''
