from time import sleep
n = 0
count = 0
som = 0
num = 0
while n != 999:
    num = int(input('Digite um valor, [999] fecha o programa: '))
    if num == 999: #limite para fechar o programa
        n = 999
        print('Você decidiu parar o programa')
    else: #nao bateu o limite
        count += 1
        som += num

    sleep(2)
print('A soma de todos os valores é igual a {}, e foi digitado {} valores'.format(som, count))

'''
    Primeiro importamos o sleep da biblioteca time (opcional)
    Criamos 4 variaveis de valor 0, para incrementar depois
    No while, enquanto n for diferente de 999, continua o loop
    A variavel num recebe um valor do usuário
    Caso num for igual a 999, o n recebe 999 que para o programa, (poderia ser usado um break), mostrando que ele parou o programa
    Caso não seja 999, count incrementa com valor 1, e som incrementa com valor num
    Por fim usa o sleep() com 2 segundos (opcional)
    E mostra a soma de todos os valores e a quantidade de valores digitados
'''
