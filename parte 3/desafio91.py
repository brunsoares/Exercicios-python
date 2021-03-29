from random import randint
from time import sleep
#biblioteca para ordenar dicionarios
from operator import itemgetter

valJog = {}

jog1 = randint(1, 6)
jog2 = randint(1, 6)
jog3 = randint(1, 6)
jog4 = randint(1, 6)

#adicionando jogadas ao dicionario
valJog['Jogador 1'] = jog1
valJog['Jogador 2'] = jog2
valJog['Jogador 3'] = jog3
valJog['Jogador 4'] = jog4

print(f'O jogador 1 tirou = {valJog["Jogador 1"]}\n'
      f'O jogador 2 tirou = {valJog["Jogador 2"]}\n'
      f'O jogador 3 tirou = {valJog["Jogador 3"]}\n'
      f'O jogador 4 tirou = {valJog["Jogador 4"]}')
sleep(2)
print('Rank das jogadas')
rank = []
#arrumando o dicionario na ordem
#Comando que organiza os dicionarios, reverse true faz com que a ordem seja trocada decrescente
rank = sorted(valJog.items(), key=itemgetter(1), reverse=True)
for pos, i in enumerate(rank):
    print(f'{pos+1} lugar: {i[0]} tirou {i[1]}')

'''
    Programa que irá sortear 4 valores e depois mostrar na ordem esses valores
    Primeiro adicionamos 3 funções de diversas bibliotecas, como:
        - O randint de random
        - O sleep de time
        - O itemgetter de operator -> esse tem a função de organizar o dicionário
    Em seguida criamos um dicionário vazio valJog, e em seguida definimos com randint() os valores de 0 a 6 dos 4 jogadores
    Depois pegamos o valJog e adicionamos em cada indice de jogador1, 2, 3 ou 4 a o seu valor, e printamos o resultado
    Usamos um sleep de 2 segundos para deixar melhor o programa, seguido de um print e a lista vazia rank
    Agora para arrumar esse dicionário usamos a lista rank, assim ele usa o sorted() de valJog nos itens (.items())
    Outro parametro é o key onde usamos o itemgetter, por fim o reverse igual a True
    Depois de ter organizado esses items com a variavel rank, usamos um for onde o pos e i irão rodar sobre o rank usando enumerate()
    Assim para cada loop será mostrado os resultados organizados
'''
