from random import randint

numComp = randint(0, 10)
print('-*- Vença o computador digitando o número que ele pensar de 0 a 10 -*-')
numPlayer = int(input('Digite um número de 0 a 10: '))

cont = 1
while numPlayer != numComp:
    numPlayer = int(input('Errou, tente novamente: '))
    cont += 1

print('\033[32mParabéns\033[m, você venceu o pc, ambos advinharam o número {} '
      'e você precisou de {} chances'.format(numComp, cont))

'''
    Nesse joguinho o usuário precisa advinhar o número que o pc escolheu
    Primeiro importamos randint da biblioteca random
    Assim já decidimos o valor do computador na variavel numComp, que usa o randint() de 0 a 10
    Em seguida é mostrado um print sobre a função do programa para o usuário, e necessitando de sua interação, que será armazenado em numPlayer
    Depois criamos uma variavel de controle com valor 1 (pois será acrescentado depois da primeira jogada do usuário)
    No while, enquanto o número do player for diferente de número do computador irá acontecer o loop
    Se for diferente o player pode tentar novamente, assim o cont acrescenta mais uma chance
    Quando sair do loop irá mostrar o print que o player venceu o pc e seu número adivinhado e quantas chances precisou
'''
