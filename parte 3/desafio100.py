from random import randint

numeros = []


def sorteia(lis):
    for i in range(0, 5):  # sortear 5 numeros e colocar na lista
        lis.append(randint(0, 50))
    print(lis)


sorteia(numeros)


def somaPar(pares):  # Somar todos os pares
    contPar = 0
    lstPar = []
    for n in pares:
        if n % 2 == 0:
            contPar += n
            lstPar.append(n)
    print(f'A lista com todos os pares é igual a = {lstPar}')
    print(f'A soma de todos os pares é igual a = {contPar}')


somaPar(numeros)  # é chamada depois de alterar a lista números

'''
    Programa sem interação do usuário, que irá sortear valores e somar esses pares e armazenar em lista
    Primeiro importamos o randint de random, e criamos uma lista numeros vazia
    Em seguida criamos a função sortear() que tem um parametro, dentro a função irá fazer um loop onde i irá rodar 5 vezes
    Em cada loop será gerado um número aleatório para ser armazenado com append() pelo lis, parametro, depois é printado por fim, porém lembrando será adicionado a lista numeros esses valores também
    Na sequência é chamado essa função usando a lista numeros vazia como parametro
    Depois criamos a somaPar() que também terá so um parametro, onde primeiramente foi criado o contPar com valor 0 e uma lista vazia lstPar
    Depois temos um for onde o n irá percorrer o parametro pares, caso o valor de n dividido por 2 restar 0, é par
    Assim o contPar incrementará esse valor e lstPar irá com append() adicionar esse valor a lista
    Por fim será mostrado ambos resultados
    Fora da função é chamado a somaPar() com o numeros (agora já adicionado os valores aleatórios) como parametro
'''
