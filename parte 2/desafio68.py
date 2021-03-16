from random import randint
print('-='*20)
print('Joguinho, par ou impar')
print('=-'*20)
win = 0
while True:
    #jogada player
    nmPlayer = int(input('Digite um valor: '))
    dec = str(input('Par ou impar? [P/I] ')).strip().upper()
    if nmPlayer > 10:
        print('Você tem mais de 10 dedos na mão???')
        print('Digite um valor válido')
        break
    #jogada comp
    nmComp = randint(0, 10)

    som = nmPlayer + nmComp

    if dec == 'P' and som % 2 == 0:
        print('\033[32mPARABÉNS\033[m, Você ganhou, você jogou {} e o computador {}, '
              'no final isso deu {} que é par'.format(nmPlayer, nmComp, som))
        win += 1
    elif dec == 'I' and som % 2 == 1:
        print('\033[32mPARABÉNS\033[m, Você ganhou, você jogou {} e o computador {}, '
              'no final isso deu {} que é impar'.format(nmPlayer, nmComp, som))
        win += 1
    else:
        print(f'\033[31mPERDEU\033[m, O computador jogou {nmComp} e você {nmPlayer} e isso deu {som}')
        break

print(f'Acabou o joguinho, você venceu {win}x do computador')

'''
    Jogo de par ou impar, para isso importamos o randint de random
    Criamos 3 prints (decorativos) para mostrar o programa
    Em seguida é criado uma variavel win de controle das vitórias do usuário
    Dentro do loop infinito, o player vai fazer duas interações, uma sobre o valor que deseja (nmPlayer) e a outra sua decisão par ou impar (dec)
    Foi usado uma verificação para ser mais parecido com o jogo real, assim limitando os números para 0 - 10
    Caso esse limite não se encaixe o programa mostra o valor inválido e em seguida é fechado
    Se o valor for válido o código continua, assim criamos a jogada do computador, nmComp que usa o randint com o mesmo limite
    E a variavel som que irá somar o número do player com o do computador
    Em seguida entra as verificações, focadas na vitória do player, a primeira caso a decisão seja 'P' (par) e a soma for dividida por 2 e restar 0 (par), o player ganhou
    Outra seria se o player colocou 'I' (impar) e a soma divida por 2 restou 1, assim sendo impar, mostrando que ganhou dessa forma também
    Em ambas o player ganha só que diferentes meios, assim mostra o resultado e incrementa a variavel win para mais 1
    Caso nenhuma das verificações bata, player perdeu assim, entra no else, onde o computador ganha mostrando os resultados
    Por fim o print é mostrado, quantas vezes o player ganhou do computador
'''
