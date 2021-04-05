#função do desafio 112, loop infinito até receber um valor monetario
def leiaDinheiro(flt):
    valido = False
    while not valido:
        entrada = str(input('Digite um valor: ')).strip().replace(',', '.')#trocando virgula por ponto
        if entrada.isalpha() or entrada == "":
            print(f'\033[31mERRO: {entrada}, não é um valor valido\033[m')
        else:
            valido = True
            return float(entrada)

'''
    Função para ler dinheiro correto
    Primeiro criamos a função leiaDinheiro() que recebe um parametro
    Em seguida colocamos a variavel valido como false
    Assim enquanto valido não for True tem loop, no loop o usuário vai interagir colocando o valor em entrada
    OBS: caso o usuário digite , no lugar de . não tem influência no valor, pois foi usado o replace()
    Caso entrada.isalpha() for True ou entrada for igual a vazio, irá gerar um erro e pedirá novamente o valor
    Caso contrário o valor é valido, assim valido fica True quebrando o loop, e será retornado um float() na entrada
'''
