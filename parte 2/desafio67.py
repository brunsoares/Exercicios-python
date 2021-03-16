from time import sleep

while True:
    val = int(input('\nDigite um número para ver sua tabuada, negativos fecharão o programa: '))
    #condição pra fechar programa
    if val < 0:
        print(f'{val} é negativo portanto programa fechando...')
        sleep(2)
        break

    for i in range(0, 11):
        calc = val * i
        print(f'{val} x {i} = {calc}')
print('Acabou a tabuada')

'''
    Programa para mostrar tabuadas, até o usuário decidir fechar
    Primeiro importamos o sleep apenas para melhorar o programa
    Dentro do loop infinito, o usuário vai digitar um valor para val
    Caso o valor seja negativo, o programa irá fechar pelo break
    Caso seja valido, vai entrar no for para  criar a tabuada, onde o i irá rodar sobre o limite de 0 a 10
    Assim cada loop no for irá usar a variavel calc que calcula o número do usuário (val) para o indice do i
    Depois é mostrado a tabuada formatada usando fstring
    Por fim quando finalizar, por parte do usuário aparecerá a mensagem que acabou o programa    
'''
