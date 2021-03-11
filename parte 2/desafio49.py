#recebendo o numero
num = int(input('Digite o número e veja sua tabuada: '))

#loop da tabuada
for n in range(1, 11):
    tab = num * n
    print('{} x {} = {}'.format(num, n, tab))

'''
    Primeiro temos a interação com usuário, assim ele digita um número inteiro que será armazenado em num
    Dentro do loop temos n que vai rodar sobre o limite de 1 até 10 (valor da tabuada)
    Assim é criado dentro do loop a variavel tab que pega o valor num digitado e multiplica pelo valor atual de n
    Além de ser printado o num, n, e tab, em formato de tabuada
'''
