import random

#Pegando valor usuario
print('O jogo é o seguinte player, escolha entre Tesoura, Pedra ou Papel, e se divirta')
player = str(input('Escolha agora: ')).capitalize().strip()

comp = ['Tesoura', 'Pedra', 'Papel']

jogComp = random.choice(comp)
#print(jogComp)

#Empate
if jogComp == player:
    print('\033[1;34mEMPATE\033[m, Ambos jogaram {}'.format(jogComp))

#Player perdendo
elif jogComp == 'Pedra' and player == 'Tesoura' or jogComp == 'Papel' and player == 'Pedra' \
        or jogComp == 'Tesoura' and player == 'Papel':
    print('\033[1;31mPERDEU\033[m, o computador ganhou com {}'.format(jogComp))

#Player ganhando
elif player == 'Tesoura' and jogComp == 'Papel' or player == 'Pedra' and jogComp == 'Tesoura' \
        or player == 'Papel' and jogComp == 'Pedra':
    print('\033[1;32mGANHOU\033[m, o computador perdeu com {}'.format(jogComp))

'''
    Um joguinho de jokenpo
    Primeiro importamos o random para o valor do computador
    Depois é mostrado um print e em seguida o usuário digita seu valor, a função capitalize() deixa a primeira letra maiuscula
    Depois é criado uma lista com valores para o computador, em comp
    E formamos a jogada do computador pelo jogComp, que irá usar a função choice() random para sortear um valor na lista
    A primeira verificação, é em caso de empate, ambos foram igual
    Em seguida tem todas as possibilidades do player perdendo, pelas regras do jogo
    E em último o player ganhando de todas as possibilidades
    Em cada verificação mostra o resultado do jogo mostrando o valor do computador
'''
