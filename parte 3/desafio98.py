from time import sleep
def contagem(ini, fim, pas): #ini = inicio, fim =  final, pas = passo
    print('-=' * 20)
    print('Contagem de 0 até 10 de 1 passo')
    for i in range(0, 11, 1): #0 até 10 de 1 em 1
        print(i, end=" ")
        sleep(1)

    print('\n')
    print('-='*20)
    print('Contagem de 10 até 0 de 2 passo')
    for i in range(10, 0, -2): #10 até 0 de 2 em 2
        print(i, end=" ")
        sleep(1)

    print('\n')
    print('-='*20)
    print('Contagem personalizada')
    for i in range(ini, fim, pas):
        print(i, end=" ")
        sleep(1)


print('-=- Vamos fazer sua contagem personalizada -=- ')
a = int(input('Digite o inicio da contagem: '))
b = int(input('Digite o fim da contagem: '))
c = int(input('Digite o passo da contagem: '))

contagem(a, b, c)

'''
    Programa que irá pegar os valores e fazer uma contagem desses valores de 3 formas
    Primeiro importamos o sleep apenas para aperfeiçoar o programa
    Em seguida criamos a função contagem() com 3 parametros, dentro a função irá realizar as contagens
    Primeiro é mostrado prints decorativos, e em seguida a primeira contagem usando o for onde irá de 0 a 10 de 1 em 1 assim o i é printado a cada loop
    Depois com o for novamente será de 10 até 0 porém contando de 2 em 2, mostrando o i a cada loop
    Por fim a contagem personalizada, onde o i do for irá percorrer o limite definido pelo usuário
    Onde o começo é a variavel ini, o final é fim e a contagem é pas, o i será mostrado em cada loop
    Fora da função, o usuário vai interagir 3 vezes, sendo a, b, c os parametros respectivamente
    Por fim é chamado a contagem() passando essas variaveis
'''
