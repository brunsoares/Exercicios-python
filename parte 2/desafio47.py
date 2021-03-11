#colocando todos os numeros pares
for i in range(1, 51):
    if i % 2 == 0:
        print(i)
print('Esses foram todos os numeros pares entre 1 e 50')

'''
    Primeiro colocamos em loop for a variavel i para rodar sobre o limite (range()) de 1 até 50, 51 pois o último número não é contado
    Dentro do loop, Caso o resto da divisão inteira de i por 2 restar 0, significa que o número é par assim será printado o i
    Quando o código sair do loop mostrará apenas um print de finalização do programa
'''
