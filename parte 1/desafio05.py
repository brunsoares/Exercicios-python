#pegando valor
num = int(input('Digite um valor inteiro: '))
numAnt = num - 1
numSuc = num + 1
print('O valor digitado é {}, seu antecessor é {}, e seu sucessor é {}'.format(num, numAnt, numSuc))

"""
Funcionamento do código

A variavel num recebe um valor inteiro;
Depois cada variavel guarda um valor, numAnt sendo o número atual - 1 e numSuc o número atual + 1;
Depois é mostrado na tela usando outro formato no print (.format())
"""
