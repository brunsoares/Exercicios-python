#função fatorial
def fatorial(num, show=False):#show é opcional para mostrar processo de calculo
    f = 1
    if show == True:
        print(num, end=" ")
        for c in range(num, 0, -1):
            f *= c
            if c != num: #so para tirar o num primeiro
                print(f'x {c}', end=" ")
        print('=', f)
    else:
        for c in range(num, 0, -1):
            f *= c
        print(f)

fatorial(5, True) #troca valores aqui
fatorial(5)

'''
    Função para calcular e mostrar formatado um cálculo fatorial
    Primeiro criamos a função fatorial() que recebe dois parametros
    OBS: o segundo é opcional, caso for True irá mostrar formatado, caso False não irá mostrar o cálculo
    Dentro da função criamos a variavel f que recebe valor 1
    Caso o segundo parametro Show for True, irá mostrar o cálculo, como nos exercícios passados de fatorial
    Caso seja false, apenas irá mostrar o resultado, assim ambos dentro do loop for para o cálculo
    Fora da função é chamada a função duas vezes uma usando parametro Show true, e a outra normal
'''
