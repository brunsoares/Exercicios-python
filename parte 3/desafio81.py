val = []
while True:
    val.append(int(input('Digite um valor: ')))
    dec = str(input('Deseja continuar? [S/N]: ')).strip().upper()
    if dec != 'S':
        break

#respostas
print(f'Essa é a lista de valores: {val}')
print(f'{len(val)} essa foi a quantidade de números digitados')
#verificando se tem 5
if 5 in val:
    print(f'O número 5 está na lista na posição {val.index(5)+1}')
else:
    print('5 não está na sua lista')
#invertendo a ordem
val.sort(reverse=True)
print(f'A lista decrescente é assim: {val}')

'''
    Esse programa irá analisar uma lista criada pelo usuário
    Primeiro criamos uma lista vazia chamada val
    Em seguida entramos no loop infinito, onde o val com o append() vai adicionar um número do usuário
    O usuário também vai interagir na variavel dec onde vai decidir se continua ou não a colocar os números
    Caso o dec for diferente de S, o loop é encerrado
    Mostrando as respostas com o print() onde o primeiro mostra a lista, o segundo mostra o tamanho da lista com o len()
    Caso tenha 5 em val irá printar a posicação de 5 usando o index()
    Caso não tenha irá printar que não tem 5 na lista
    Por fim usou o sort() com parametro reverse=True para organizar a lista de forma crescente no reverso, no caso decrescente
    Em seguida é printado
'''
