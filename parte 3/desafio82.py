valGer = []
valPar = []
valImp = []

while True:
    valGer.append(int(input('Digite um valor: ')))
    dec = str(input('Deseja continuar? [S/N]: ')).strip().upper()
    if dec != 'S':
        break

#verificações
for i in valGer:
    if i % 2 == 0:
        #print('É par')
        valPar.append(i)
    if i % 2 == 1:
        #print('É impar')
        valImp.append(i)


print(f'Essa é a lista geral -> {valGer}')
print(f'Essa é a lista par -> {valPar}')
print(f'Essa é a lista impar -> {valImp}')

'''
    Esse programa irá analisar uma lista de números do usuário e separar em par e impar os valores
    Primeiro criamos 3 listas vazias, valGer, valPar, valImp
    Em seguida entramos no loop infinito, onde valGer usando o append() adiciona o valor do usuário na lista
    Depois temos o dec para saber a decisão do usuário, onde diferente de S irá parar o loop
    No loop for o i irá rodar sobre o valGer, caso o i dividido por 2 restar 0, é par e será adicionado esse número a lista par pelo append()
    Caso o i dividido por 2 restar 1, é impar e será adicionado esse número a listar impar pelo append()
    Depois é printado as 3 listas para comparar
'''
