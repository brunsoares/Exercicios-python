val = []
valPar = []
valImpar = []

for i in range(0, 7):
    num = int(input('Digite um valor: '))
    if num % 2 == 0: #Par
        valPar.append(num)
    elif num % 2 == 1: #impar
        valImpar.append(num)

#Adicionando a lista principal
val.append(valPar)
val.append(valImpar)
print(f'Essa é a lista par {sorted(val[0])}\n'
      f'Essa é a lista impar {sorted(val[1])}')

'''
    Programa que irá analisar uma lista do usuário de 7 valores, e separar par e impar ordenados
    Primeiro criamos 3 listas, val, valPar e valImpar
    Dentro do loop o i irá rodar sobre um limite de 0 a 6, dentro do loop o usuário digita um valor armazenado em num
    Caso o num dividido por 2 restar 0, é par e será adicionado pelo append() no valPar
    Caso o num dividido por 2 restar 1, é impar e será adicionado pelo append() no valImpar
    Por fim val da append() em ambos, valPar e valImpar
    E o print mostra ambos ordenados pelo sorted()
'''
