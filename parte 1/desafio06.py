#pegando numero
num = int(input('Digite um número qualquer: '))
numDob = num * 2
numTri = num * 3
numRaiz = num**(1/2) #Raiz quadrada é o mesmo que o numero elevado ao meio 1/2
print('O número digitado foi {}, seu dobro é {}, seu triplo é {}, e por fim sua raiz é {}'.format(num, numDob, numTri, numRaiz))

'''
    A variavel num recebe um inteiro do usuário, numDob faz o número atual * 2,
    O numTri faz o número atual * 3 e numRaiz faz a raiz do número atual (num elevado a 0,5)
    E o resultado é printado no final
'''
