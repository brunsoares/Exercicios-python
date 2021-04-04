def notas(*n, sit=False):
    qunt = len(n) #quantidade de notas
    mai = max(n) #maior nota
    men = min(n) #menor nota
    o = 0 #soma das notas
    for i in n:
        o += i
    md = o / len(n) #media

    if sit == True:
        if md < 7:
            situ = 'REPROVADOS'
            return {'Quantidade notas': qunt, 'Maior nota': mai, 'Menor nota': men, 'Média': md, 'Situação': situ}
        elif md >= 7:
            situ = 'APROVADOS'
            return {'Quantidade notas': qunt, 'Maior nota': mai, 'Menor nota': men, 'Média': md, 'Situação': situ}

    return {'Quantidade notas': qunt, 'Maior nota': mai, 'Menor nota': men, 'Média': md}

val = notas(5.5, 3, 3.6, 10, 9.5, sit=True) #colocar sit=True para ver a situação
print(val)

'''
    Função que checa a situação de notas de uma sala
    Primeiro criamos a função notas() que recebe um todos os valores do parametro (*) e um opcional com valor False inicial
    Dentro criamos 3 variaveis, sendo qunt o len() de n, mai sendo o max() de n, e min sendo o min() de n, e n é o valor do parametro
    Por fim a variavel 'o' com valor 0
    No for o i irá rodar sobre o n, que é uma tupla, Assim cada loop a variavel 'o' incrementa i
    Por fim tiramos a media, variavel md que pega o 'o' e divide pelo len() de n
    Caso o segundo parametro for true, ele mostrará a situação, assim entra no if
    Caso a md for menor que 7, a variavel situ recebe valor REPROVADOS, caso contrário recebe valor APROVADOS
    Em ambos os casos é retornado um dicionário contendo o valor de cada indice, incluindo a situação
    Caso o segundo parametro não for true, ele retornará um dicionário com as informações exceto a situ
    Fora da função temos a variavel val que chama a função notas, que recebe uma tupla de valores, e com opcional True
    Por fim é printado val
'''
