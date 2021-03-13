from time import sleep

#pegando os números
nm1 = float(input('Digite o primeiro valor: '))
nm2 = float(input('Digite o segundo valor: '))

sair = 0

while sair != 5:
    print('\nSeus números são {} e {}, o que você quer fazer?\n'.format(nm1, nm2))
    print('-*-' * 5, 'Menu', '-*-' * 5)
    print('[1] para \033[32mSomar\033[m\n'
          '[2] para \033[35mMultiplicar\033[m\n'
          '[3] para \033[33mMaior\033[m\n'
          '[4] para \033[36mNovos números\033[m\n'
          '[5] para \033[31mSair do programa\033[m')
    dec = int(input('\nQual você deseja? '))
    #somando
    if dec == 1:
        som = nm1 + nm2
        print('A soma de {} + {} = {}'.format(nm1, nm2, som))
        #sair = 5
    #multiplicando
    if dec == 2:
        mult = nm1 * nm2
        print('A multiplicação entre {} x {} = {}'.format(nm1, nm2, mult))
        #sair = 5
    #maior número
    if dec == 3:
        maior1 = nm1 > nm2
        maior2 = nm1 < nm2
        if maior1 == True:
            print('O número {} é maior que o número {}'.format(nm1, nm2))
        elif maior2 == True:
            print('O número {} maior que o número {}'.format(nm2, nm1))
        else:
            print('Ambos os números tem o mesmo valor')
        #sair = 5
    #novos números
    if dec == 4:
        nm1 = float(input('Digite um novo primeiro número: '))
        nm2 = float(input('Digite um novo segundo número: '))
        #print(nm1, nm2)
        #sair = 5
    #sair do programa
    if dec == 5:
        print('\033[31mADEUS\033[m, meu caro ;-;')
        sair = 5

    #Função apenas para aperfeiçoar o app deixando melhor para o usuario
    sleep(2)

'''
    Esse programa é uma calculadora simples, que pode ser melhorada
    Primeiro importamos o sleep da biblioteca time, apenas para deixar mais amigavel o programa
    Em seguida pegamos dois valores do usuário armazenados em nm1, nm2, e criamos uma variavel de controle sair com valor zero
    Enquanto no while a o sair for diferente de 5 continuará o loop
    Assim é mostrado ao usuário seus números e um menu básico para o que ele escolherá fazer com os números
    Depois é pego a decisão do usuário armazenado em dec
    Assim cada número de 1 - 5 tem sua função mostrada nos if's, quando esse valor for decidido pelo usuário entrará no if
    Todas as funções mostram o resultado e depois voltam ao menu, apenas termina o programa se o usuário decidir sair
'''
