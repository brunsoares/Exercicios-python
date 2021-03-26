from random import randint

#Pegando total de palpites do usuario
palp = int(input('Digite quantos palpites você quer que sejam gerados: '))

allPalp = []
dadosPalp = []
totalPalp = 0

while totalPalp <= palp-1:
    cont = 0
    while True: #loop infinito
        num = randint(1, 60)
        if num not in dadosPalp:#se o número não estiver na lista adiciona evita repetidos
            dadosPalp.append(num)
            cont += 1
        if cont >= 6:
            break

    allPalp.append(dadosPalp[:])
    dadosPalp.clear()
    totalPalp += 1
#mostrando resultado bonito
for pos, i in enumerate(allPalp):
    print(f'Jogo {pos+1}:     {i}')

'''
    Esse programa vai gerar 6 valores random, que você pode usar para apostar hehe
    Primeiro importamos o randint da biblioteca random
    Em seguida pegamos um valor do usuário armazenado em palp
    Depois criamos 2 listas vazias e uma variavel de controle zerada
    Dentro do loop enquanto o totalPalp for menor ou igual a palp -1 o loop irá ocorrer
    No loop criamos outra variavel de controle cont zerada
    Depois entra em um loop infinito onde a variavel num vai armazenar um valor de 1 a 60
    Caso o num não esteja nos dadosPalp ele será adicionado, evitando repetidos, cont é acrescentado 1
    Caso o cont for maior ou igual a 6 para esse loop infinito
    Em seguida o allPalp com append() cria uma copia de dadosPalp, para que essa seja limpa com o clear(), o totalPalp incrementa 1
    Por fim é mostrado o resultado dentro do for, onde o pos e i irão rodar o allPalp usando enumerate()
'''
