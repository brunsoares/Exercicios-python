import random

#colocando o nome dos alunos
a1 = input('Digite o nome do primeiro aluno: ')
a2 = input('Digite o nome do segundo aluno: ')
a3 = input('Digite o nome do terceiro aluno: ')
a4 = input('Digite o nome do quarto aluno: ')

#colocando a lista de alunos
lista = [a1, a2, a3, a4]

#Sorteando
random.shuffle(lista)

print('Atenção, essa será a lista da apresentação de hoje: {}'.format(lista))

'''
    Novamente usamos random, e primeiro importamos ele
    Depois o usuário vai digitar nomes dos alunos que serão armazenados em a1, a2, a3, a4
    A variavel lista vai colocar em LISTA os valores, lista básicamente uma forma de variavel composta, mostrada depois nos exercicios
    Depois usamos o shuffle() para embaralhar os nomes em alguma ordem, não tem nenhuma variavel armazenando esse valor
    Pois o shuffle altera a variavel que ele embaralhou, assim podemos usar a variavel lista normalmente
    E depois printamos a lista embaralhada
'''
