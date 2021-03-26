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

matriz.append(fLine)
matriz.append(sLine)
matriz.append(tLine)
#print(matriz)
#mostrando formato de matriz 3x3
print(f'[{matriz[0][0]}] [{matriz[0][1]}] [{matriz[0][2]}]')
print(f'[{matriz[1][0]}] [{matriz[1][1]}] [{matriz[1][2]}]')
print(f'[{matriz[2][0]}] [{matriz[2][1]}] [{matriz[2][2]}]')

'''
    Programa que irá gerar uma matriz 3x3 no formato, usando valores do usuário
    Primeiro criamos 4 listas vazias, uma para englobar todas as linhas matriz e as linhas matriz
    Em seguida entramos em um for em que o i irá rodar 3 vezes o loop (um para cada número da linha)
    No loop o usuário interage com o valor, e esse valor é adicionado na linha da matriz (fLine, sLine, tLine) com append()
    Isso ocorre para as 3 linhas, por fim a matriz pega com append() esses 3 valores
    E depois é printado todos os resultados no formato de matriz    
'''
