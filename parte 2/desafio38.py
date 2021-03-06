#pegando numeros do usuario
val1 = int(input('Digite o primeiro valor: '))
val2 = int(input('Digite o segundo valor: '))

if val1 > val2:
    print('O valor {} é maior que o {}'.format(val1, val2))
elif val1 < val2:
    print('O valor {} é maior que o {}'.format(val2, val1))
else:
    print('Tanto o valor {} quanto {} são iguais'.format(val1, val2))

'''
    O usuário vai digitar dois valores, armazenados em val1 e val2
    A verificação será aninhada, ou seja usando if, elif, else
    No caso do if será se o val1 for maior que val2
    Caso não seja True, vai passar para o elif que analisará se o val1 é menor que o val2
    Caso também não bata, vai cair no else que seria os dois valores iguais
    Em cada verificação será mostrado um print com base na verificação
'''
