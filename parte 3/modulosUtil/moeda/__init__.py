# modulo moeda.py
# Exercicio 108 formatar print numerico
def moeda(val):
    print(f'R$ {val:.2f}')


# Func de aumentar uma porcentagem
def aumentar(n, aum, mod=False):
    # Aum ta em % então dividir por 100 e multiplicar pelo n
    aumento = (aum / 100) * n
    if mod == True:
        moeda(n + aumento)
    else:
        return n + aumento



# func de diminuir uma porcentagem
def diminuir(n, dim, mod=False):
    dimin = (dim / 100) * n
    if mod == True:
        moeda(n - dimin)
    else:
        return n - dimin


# func de dobrar valor
def dobrar(n, mod=False):
    if mod == True:
        moeda(n * 2)
    else:
        return n * 2


# func de metade do valor
def metade(n, mod=False):
    if mod == True:
        moeda(n / 2)
    else:
        return n / 2


# func de resumo
def resumo(nms, sob, des):
    print('-=- Resumo mostrado -=-')
    print(f'Preço analisado = ', end="")
    moeda(nms)
    print(f'Dobro do preço = ', end="")
    dobrar(nms, True)
    print(f'Metade do preço = ', end="")
    metade(nms, True)
    print(f'Com {sob}% de aumento = ', end="")
    aumentar(nms, sob, True)
    print(f'Com {des}% de desconto = ', end="")
    diminuir(nms, des, True)

'''
    Arquivo que contém as funções usadas do exercício 107 ao 110
    Arquivo que realmente foi usado, diferente do desafio107mod.py, explicação das funções:
    Primeiro temos a função moeda, recebe um parametro e apenas mostra-o formatado em R$
    Depois temos a função a função aumentar que recebe 3 parametros, um opcional
    Dentro o aumento recebe o aum dividido por 100 e depois multiplicado por n, valor do aumento
    Caso o parametro mod for true, ele mostrará formatado usando a função moeda(), caso for false apenas retorna o valor aumentado
    A proxima função diminuir, faz bem parecido com o aumentar, porém ela invés de somar com o valor n, ela subtrai, assim descontando
    A função dobrar recebe n, onde apenas faz com que n seja multiplicado por 2, duplicando o valor
    E contrapartida temos a metade, que ao receber n, o divide por 2 assim gerando a metade
    Por fim temos a função resumo, onde essa onde recebe 3 parametros, que são usados nas outras funções
    Essa função tem como funcionalidade resumir todas as outras funções, e mostrar seus resultados, com o mod=True
    OBS: todas as funções tem o parametro mod=False, como opcional, esse parametro apenas pede para que seja true se o usuário quer ver formatado em moeda
    Caso True, chamará a função moeda() que formatará como já foi visto
'''
