#import desafio107mod
from modulosUtil import moeda

num = int(input('Digite um valor: '))
print('O aumento de 10% deu: ', end="")
#desafio107mod.aumentar(num, 10, True)
moeda.aumentar(num, 10, True)
print('\nO desconto de 10% deu: ', end="")
#desafio107mod.diminuir(num, 10, True)
moeda.diminuir(num, 10, True)
print('\nA metade desse valor é: ', end="")
#print(desafio107mod.metade(num))
print(moeda.metade(num))
print('\nO dobro desse valor é: ', end="")
#print(desafio107mod.dobrar(num))
print(moeda.dobrar(num))
#exercicio que pede para colocar um parametro a mais para ver se vai ser formatado em R$ ou n
#Nos que quiser ver o formatação de dinheiro colocar True em segundo parametro
#Sem formatação estar entre print()

'''
    Programa igualmente o 108, porém no lugar de colocar a função moeda() para formatar
    É usado um parametro, opcional, que quando colocado True, mostra formatado
    Apenas foi acrescentado nas funções, juntamente de suas explicações
'''
