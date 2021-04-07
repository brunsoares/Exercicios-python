from modulosUtil import dados, moeda

val = dados.leiaDinheiro('Digite um valor: ')
moeda.resumo(val, 10, 10)

'''
    Esse programa é muito semelhante ao 110, porém usamos as duas bibliotecas, dados e moeda
    Após importar essas bibliotecas, a variavel val recebe o valor do usuário, porém esse valor, já tem a verificação da função dentro de dados
    Com isso é chamado o resumo() dentro de moeda
    Por fim é mostrado tudo pelas funções
'''
