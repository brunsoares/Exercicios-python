import random

#pegando o nome dos alunos
aluno1 = input('Digite o nome do primeiro aluno: ')
aluno2 = input('Digite o nome do segundo aluno: ')
aluno3 = input('Digite o nome do terceiro aluno: ')
aluno4 = input('Digite o nome do quarto aluno: ')

#Sorteador
sort = random.choice([aluno1, aluno2, aluno3, aluno4])
print('{}, Por favor apague o quadro de anotações'.format(sort))

'''
    Nesse usamos a biblioteca random, que randomiza seus valores para uma diversificação do código
    Primeiro importamos essa bibliota com import random
    Em seguida as variaveis aluno1, 2, 3, 4, recebem o nome dos alunos pelo usuário
    A variavel sort vai usar a função choice() para escolher um valor da LISTA (será um assunto mostrado depois)
    Lista são os [] dentro do choice()
    Depois o print mostra quem foi escolhido, cada vez que o programa for iniciado será diferente
'''
