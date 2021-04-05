#from desafio107mod import resumo
from modulosUtil import moeda

valorUsu = float(input('Digite um valor: '))
#resumo(valorUsu, 10, 10)
moeda.resumo(valorUsu, 10, 10)

'''
    Programa que resume todos os outros programas em apenas 3 linhas de código
    Onde foi criado no arquivo de funções outra função chamada resumo()
    Essa por sua vez resume todas as informações das demais funções e passa o resultado
    No programa apenas pedidos o valor e já chamamos na biblioteca moeda a função resumo()
    Que passa esses valores, os 10 é para acrescentar 10% e descontar 10%, nessa mesma ordem
'''
