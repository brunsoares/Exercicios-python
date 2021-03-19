#Pegando dados do exercicio
itns = ('Lápis', 1.75, 'Borracha', 2,
        'Caderno', 15.90, 'Estojo', 25,
        'Transferidor', 4.20, 'Compasso', 9.99,
        'Mochila', 120.32, 'Canetas', 22.30, 'Livros', 34.90)

print('-*-'*20, '\n{:^60}\n'.format('Lojinha hehe'), '-*-'*20)

for pos, i in enumerate(itns):
    #Itens em pos par é o nome dos itens
    if pos % 2 == 0:
        print('{:.<40}'.format(i), end="")
    #itens em pos impar é o prço dos itens
    if pos % 2 == 1:
        print('R$ {:>7.2f}'.format(i))

print('='*60)

'''
    Outro programa sem interação do usuário, apenas para deixar organizado
    Primeiro criamos uma tupla organizada da seguinte forma ('objeto', preço), armazenada em itns
    Depois criamos um print decorativo
    E em seguida entra no loop usando duas variaveis, pos e i em enumerate que irá rodar itns
    Se o pos dividido por 2 restar 0, ou seja indice par, é os objetos, onde serão printados alinhados a esquerda
    Caso o pos dividido por 2 restar 1, ou seja indice impar, é os preços, serão printados alinhados a direita
    Por fim um print separando e finalizando a tabela
'''
