#from desafio107mod import *
from modulosUtil import moeda

num = int(input('Digite um valor: '))
print('O aumento de 10% deu: ', end="")
#moeda(moeda.aumentar(num, 10))
moeda.moeda(moeda.aumentar(num, 10))
print('O desconto de 10% deu: ', end="")
#moeda(moeda.diminuir(num, 10))
moeda.moeda(moeda.diminuir(num, 10))
print('A metade desse valor é: ', end="")
#moeda(moeda.metade(num))
moeda.moeda(moeda.metade(num))
print('O dobro desse valor é: ', end="")
#moeda(moeda.dobrar(num))
moeda.moeda(moeda.dobrar(num))
#moeda() é apenas para formatar em moeda os valores

'''
    O mesmo programa que o exercício passado, 107, porém mostrando o valor formatado e usando outro caminho
    Apenas foi usado a função o caminho da biblioteca moeda, assim dentro de moeda, achar a função moeda, assim passando os valores com base nas funções
    Ex: moeda.moeda(moeda.diminuir(num,10))
        Biblioteca.função(biblioteca.função(parametros da função))
'''
