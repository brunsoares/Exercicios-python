#importando random
from random import randint

numComp = randint(0, 5)

#pegando numero usuario
print('O jogo eh o seguinte, o computador advinhou um numero inteiro entre 0 - 5\n'
      'Sua missão, é acertar esse número, você tem 16,66% de chance')
numUsu = int(input('Acerte o número: '))

if numComp == numUsu:
    print('Parabéns você acertou o número, ambos colocaram {}'.format(numComp))
else:
    print('ERROU, tente novamente, o número foi {}'.format(numComp))

'''
    O primeiro programa usando condição, estrutura if/else
    Primeiro já que usaremos randomização no programa importamos o randint
    OBS: não importamos o random inteiro, e sim o randint, que é uma função dentro do random
    Depois a variavel numComp pega um valor random entre 0 - 5
    Depois aparece um print mostrando ao usuário o que fazer, e em seguida um input que fará ele colocar um número armazenado em numUsu
    Em seguida chega a verificação, usando if, sendo essa verificação, se o número do computador for IGUAL ao número do usuário, faça algo
    Caso contrario, o else, faça outra coisa
    *Sempre o if vai tratar de uma informação True, e o else de uma False*
    *Toda verificação precisa de um if, mas não necessariamente de um else*
    No programa, caso for verdade (True/if) vai printar mostrando que o usuário venceu
    Caso contrario (False/else) vai printar que errou o resultado, ambos mostrando o numComp
'''
