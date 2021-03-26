#aprimoramento do desafio anterior
matriz = []
fLine = []  #primeira linha da matriz   [ ] [ ] [ ]
sLine = [] #segunda linha da matriz     [ ] [ ] [ ]
tLine = [] #terceira linha da matriz    [ ] [ ] [ ]

for i in range(0, 3): #for para primeira linha
    num = int(input(f'Digite um número para [0][{i}] da matriz: '))
    fLine.append(num)

for i in range(0, 3): #for para a segunda linha
    num = int(input(f'Digite um número para [1][{i}] da matriz: '))
    sLine.append(num)

for i in range(0, 3): #for para a terceira linha
    num = int(input(f'Digite um número para [2][{i}] da matriz: '))
    tLine.append(num)

matriz.append(fLine[:])
matriz.append(sLine[:])
matriz.append(tLine[:])
#print(matriz)
#mostrando formato de matriz 3x3
print(f'[  {matriz[0][0]}  ] [  {matriz[0][1]}  ] [  {matriz[0][2]}  ]')
print(f'[  {matriz[1][0]}  ] [  {matriz[1][1]}  ] [  {matriz[1][2]}  ]')
print(f'[  {matriz[2][0]}  ] [  {matriz[2][1]}  ] [  {matriz[2][2]}  ]')

#Até aqui era o desafio 86, a partir daqui começa o 87

#verificação de par, na fLine
somPar = 0
for i in matriz[0]:
    if i % 2 == 0:
        somPar += i
for i in matriz[1]: #sLine
    if i % 2 == 0:
        somPar += i
for i in matriz[2]: #tLine
    if i % 2 == 0:
        somPar += i

#soma na terceira coluna
somTCol = matriz[0][2] + matriz[1][2] + matriz[2][2]

print(f'A soma de todos os itens pares dá {somPar}')
print(f'A soma de todos os itens da terceira coluna é {somTCol}')
print(f'O maior valor da segunda linha é {max(matriz[1])}')

'''
    Aprimoramento do exercício anterior 86
    Ao terminar o exercício 86, começa a esse exercício onde primeiro criamos a somaPar onde vai receber valor 0
    Assim entramos no loop for onde o i vai percorrer o limite de cada linha da matriz
    Onde o i dividido por 2 restar 0, a somaPar vai acrescentar o i
    Depois o somTCol vai somar a 3° coluna inteira
    Por fim os resultados são mostrados no print onde o último print usa o max() para mostrar o maior valor da segunda linha
'''
