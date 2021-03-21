#pegando os valores na lista
val = []
posi = 0
for i in range(0, 5):
    val.append(int(input(f'Digite um valor para a lista, na posição {posi}: ')))
    posi += 1

print(f'Esse foi o maior valor: \033[32m{max(val)}\033[m que está na posição {val.index(max(val))}\n'
      f'Esse foi o menor valor: \033[32m{min(val)}\033[m que está na posição {val.index(min(val))}')

'''Outra forma de fazer
#pegando os valores na lista
val = []
posi = 0
menor = 0
maior = 0
menorPos = 0
maiorPos = 0
for i in range(0, 5):
    val.append(int(input(f'Digite um valor para a lista, na posição {posi}: ')))
    posi += 1
    for pos, usu in enumerate(val): #usu é o valor na lis e pos eh a posicao do indice
        if pos == 0: #primeiro numero
            maior = usu
            menor = usu
            maiorPos = pos
            menorPos = pos
        if pos != 0: #outros numeros
            if usu > maior:
                maior = usu
                maiorPos = pos
            if usu < menor:
                menor = usu
                menorPos = pos

print(f'Esse foi o maior valor: \033[32m{maior}\033[m que está na posição {maiorPos}\n'
      f'Esse foi o menor valor: \033[32m{menor}\033[m que está na posição {menorPos}')
#(maiorPos)
#print(menorPos)'''

'''
    Programa para analisar o maior valor e menor de uma tupla criada pelo usuário, feito de duas formas, primeiro exercício de lista
    Primeiro criamos a variavel val que é uma lista vazia, e posi que começa com valor 0
    No loop o i irá rodar sobre o limite de 5 vezes, 0-5
    Dentro do loop o usuário vai interagir colocando valores na lista, usando o append()
    E a posi incrementa 1
    Por fim o print irá mostrar os resultados, assim pegando o valor máximo com o max() e o minimo com o min()
    Já a posição encontra com o index, ou seja, index(max()) e index(min())
'''
