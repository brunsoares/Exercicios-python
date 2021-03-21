#loop infinito
val = []
while True:
    v = int(input('Digite um valor: '))
    if v not in val:
        val.append(v)
    else:
        print('\033[31mNúmero invalido, duplicado! \033[m', end="")
    dec = str(input('Deseja continuar [S/N]: ')).strip().upper()
    if dec != 'S':
        break

val.sort()
print(f'Os números mostrados foram: {val}')

'''
    Programa para listar os valores, porém não permite valores duplicados
    Primeiro criamos uma lista vazia, armazenada em val
    Depois dentro do loop infinito o usuário vai digitar um valor armazenado em v
    Caso o v não esteja (not in) em val, o valor é adicionado com o append()
    Caso já exista cai no else onde é mostrado que o número é inválido
    Depois tem uma interação, onde o usuário vai digitar se deseja continuar ou não, armazenado em dec
    Caso o valor seja diferente de S o loop é parado
    Por fim a lista val é ordenada crescente, usando o sort(), e printada com o print()
'''
