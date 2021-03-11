from time import sleep

cont = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

#Contagem de fogos 10 - 0
print('\033[32mPREPARE-SE\033[m, contagem para fogos em:')
for c in list(cont): #tambem funcionaria range(10, -1, -1) Quando passo for -1 ele fica ao contrario
    print(c)
    sleep(1)
print('Acabou ;-;')

'''
    Para esse exercício foi importado o sleep da biblioteca time apenas para deixar mais dinâmico o programa
    Primeiro criamos uma lista [] com valores de 10 até 0 armazenado em cont
    Depois é mostrado um print decorativo
    E começa usando um laço de repetição, o for, que consiste em um loop até que a condição se torne falsa
    Ou seja, for c (variavel criada apenas para rodar no for) in list(cont) (função para a variavel c rodar sobre todos os indices da lista)
    Assim sobre cada indice (No caso os números de cont) ele vai printar c que mostrará o número, e depois dormirá com sleep() por 1 segundo
    Quando a condição se tornar falsa, ou seja, c rodou sobre todos os indices, o código sai do loop e cai no print finalizando o programa
    OBS: da para fazer de outras formas como o range(10, -1, -1)
'''
