maior = 0
menor = 0
som = 0
count = 0
dec = 'S'
while dec != 'N':
    num = int(input('Digite um valor: '))
    dec = str(input('Deseja continuar: [S/N] ')).upper()
    som += num
    count += 1

    #maior e menor
    if count == 1: #primeiro valor, eh o menor e o maior, pois não tem outros
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

    if dec == 'N':
        print('Você decidiu parar o programa')
    if dec != 'S' and dec != 'N':
        print('Digite um valor válido')
        dec = 'N'

md = som / count

print('A média dos valores é {:.2f}, e o maior valor foi {},e o menor foi {}'.format(md, maior, menor))

'''
    Programa para ver maior e menor valores digitados e sua média
    Primeiro criamos 5 variaveis de controle, todas com valor 0, exceto dec com valor 'S'
    No while, enquanto dec for diferente de 'N', vai ter loop
    Assim o usuário vai interagir colocando valores em num e dec
    A variavel som acrescenta o número adicionado, e a variavel count acrescenta 1
    Para verificar o maior e menor foi usado um if, que caso count seja 1 (primeiro valor), ele será o maior e menor
    Ou seja maior e menor recebe num
    Caso caia no else (count diferente de 1), entra em outro if, que caso o num for maior que maior, o maior receberá num
    O mesmo caso para o num for menor que menor, onde essa variavel vai receber num
    Caso o dec for igual a 'N', irá finalizar o programa
    E caso não seja nem 'S' nem 'N', o programa irá finalizar mostrando que a dec foi um valor invalido
    Por fim a média é tirada na variavel md, onde pega som e divide pelo count
    No print é mostrado os resultados de média, valores maior e menor
'''
