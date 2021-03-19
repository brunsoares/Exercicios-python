from random import randint

nm1 = randint(0, 20)
nm2 = randint(0, 20)
nm3 = randint(0, 20)
nm4 = randint(0, 20)
nm5 = randint(0, 20)

#print(nm1, nm2, nm3, nm4, nm5)

tupla = (nm1, nm2, nm3, nm4, nm5)
#print(tupla)

#Deixando em ordem númerica
tupOrd = sorted(tupla)
#print(tupOrd)

#maior e menor
#print(tupOrd[4])
#print(tupOrd[0])

print(f'Os número sorteados foram: {tupla}\n'
      f'Em ordem fica: {tupOrd}\n'
      f'Maior foi {tupOrd[4]} e o menor {tupOrd[0]}')

'''
      Esse programa serve para aleatorizar uma tupla
      Primeiro importamos o randint() de random
      Em seguida definimos 5 variaveis entre nm1 a nm5 que receberão um número aleátorio entre 0 e 20
      Assim depois é criado uma tupla contendo essas 5 variaveis
      A variavel tupOrd deixa a tupla em ordem pelo sorted()
      Por fim o print mostra os números na tupla, a tupla ordenada, e o maior e menor número
      Programa sem interação do usuário
'''
