import math

#Pegando numero
print('Formato do número real = 00.00')
num = float(input('Digite um número real: '))
#mostrando apenas a parte inteira
int = math.trunc(num)

print('Seu número é {}, e sua parte inteira é {}'.format(num, int))

'''
    Primeiro exercicio usando bibliotecas externas
    Primeiro usamos o import (na primeira linha) para importar a biblioteca math, que por padrão vem no pycharm, porém outras tem que instalar externamente
    A variavel num recebe um float do usuario
    A varivael int usa uma função dentro da biblioteca math, o trunc() que serve para achar a parte inteira de um número
    O int pega essa parte inteira e armazena na variavel
    Logo depois é printado as variaveis num e int, onde da para comparar o uso do trunc()
'''
