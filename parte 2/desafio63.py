#pegando num
n = int(input('Digite um valor: '))
#valores padrao da fibonacci
t1 = 0
t2 = 1
print('{} -> {} -> '.format(t1, t2), end='')
count = 3 #pois vai começar a contar da 3 posição
while count <= n:
    t3 = t1 + t2
    print('{} -> '.format(t3), end="")
    #trocando as posições para o proximo calculo, ou seja t1 vai ser t2 e t2 vai ser t3
    #e depois calcula o t3 novamente no loop
    t1 = t2
    t2 = t3
    count += 1
print('Acabou')

'''
    Programa sobre a sequência fibonacci
    Primeiro pegamos um valor do usuário, armazenado em n
    Depois criamos variaveis t1 e t2 com valores padrões da sequência fibonacci, t1 = 0, t2 = 1
    Depois é printado esses valores e criado a variavel count com valor 3, para começar da 3° posição
    No while, enquanto count for menor ou igual a n continua o loop
    É criado uma variavel t3 com valor de t1 e t2, mostrando t3 ta tela
    Depois Trocando valores, onde o t1 recebe t2 e t2 recebe t3
    Incrimentando no count por fim
    Quando sair do loop é mostrado print finalizando programa
'''
