from time import sleep

baratNM = ''
barat = 0
prodMil = 0
preTot = 0
idnt = 0
while True:
    #info produto
    idnt += 1
    nmProd = str(input('Digite o nome do produto: ')).strip().capitalize()
    preco = float(input('Digite o preço desse produto: R$'))
    dec = str(input('\nVocê quer continuar comprando? [S/N] ')).strip().upper()
    while dec != 'S' and dec != 'N':
        print('\033[31mValor inválido, digite corretamente\033[m')
        dec = str(input('Você quer continuar comprando? [S/N] ')).strip().upper()

    #validações
    preTot += preco
    #print(preTot)

    #preço mais barato
    if idnt == 1: #primeiro produto
        barat = preco
        baratNM = nmProd
    else:#outro produto
        if preco < barat: #preço menor que o anterior mudar
            barat = preco
            baratNM = nmProd

    #preco mais de mil
    if preco > 1000:
        prodMil += 1
        #print(prodMil)

    #fechando programa
    if dec == 'N':
        print('Fechando carrinho aguarde.')
        sleep(4)
        break

print(f'\nO total do carrinho chegou em R${preTot:.2f}')
print('Desse carrinho {} produtos são mais de R$1000.00\n'
      'O produto mais barato do carrinho é: \033[34m{}\033[m que custa R${:.2f}'.format(prodMil, baratNM, barat))

'''
    Primeiro importamos o sleep (opcional)
    Em seguida criamos 5 variaveis de controle, onde todas estão zeradas, exceto baratNM onde está ''
    Dentro do loop infinito, incrementamos a variavel idnt para mais 1, assim sendo o identificador de cada produto
    Depois o usuário interage com 3 valores o nome do produto nmProd, o valor preco, e se deseja continuar dec
    Caso o valor de dec for inválido, será usado o mesmo loop do exercício anterior para pegar um valor correto
    Depois pegamos a variavel preTot que incrementará o preço dos produtos
    Depois vamos atrás do preço mais barato e pegar esse nome do produto
    Primeiro caso se o idnt for o primeiro, esse produto será o mais caro e o mais barato, pois é o primeiro
    Assim barat recebe preco, preço do produto, e baratNM recebe o nmProd, nome do produto
    Caso não seja o idnt 1 (primeiro produto), ele checará se o produto atual tem preço menor que o anterior
    Caso seja verdade o barat recebe esse preco atual, e o mesmo para o baratNM que receberá o nmProd atual
    Caso um produto tenha valor maior que 1000, a variavel prodMil incrementará com mais 1
    Por fim se o usuário digitar a decisão (dec) e for igual a 'N' o loop fechará
    Assim mostrando os resultados pelo print()
'''
