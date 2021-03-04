#pegando numero usuario
num1 = int(input('Digite um valor: '))
num2 = int(input('Digite outro valor: '))
num3 = int(input('Digite ultimo valor: '))

#Checando num1 maior
if num1 >= num2 and num1 >= num3:
    print('O maior número é {}'.format(num1))
    if num2 > num3:
        print('O menor número é {}'.format(num3))
    else:
        print('O menor numero é {}'.format(num2))

#checagem do num2 maior
if num2 >= num1 and num2 >= num3:
    print('O maior número é {}'.format(num2))
    if num1 > num3:
        print('O menor número é {}'.format(num3))
    else:
        print('O menor número é {}'.format(num1))

#checagem do num3 maior
if num3 >= num1 and num3 >= num2:
    print('O maior número é {}'.format(num3))
    if num1 > num2:
        print('O menor número é {}'.format(num2))
    else:
        print('O menor número é {}'.format(num1))

'''
    Checagem para ver qual número é maior e menor
    Primeiro pegamos 3 valores do usuário, que serão armazenados em num1, num2, num3
    Depois Usamos cada checagem para ver qual número é maior, para cada caso
    Após achar o maior entra em outro if para achar o menor
    Assim tem a verificação completa de todos os valores
    Em cada caso é printado o maior e menor valor, dependendo da verificação
'''
