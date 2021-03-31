def escreva(txt):
    print('~'*len(txt))
    print(txt)
    print('~'*len(txt))


f1 = str(input('Digite uma frase: ')).strip().title()
f2 = str(input('Digite outra frase: ')).strip().title()
f3 = str(input('Digite mais uma frase: ')).strip().title()
escreva(f1)
escreva(f2)
escreva(f3)

'''
    Programa que mostra um texto personalizado
    A função escreva definida com parametro txt, irá printar 3 vezes, a primeira  e a última apenas para decorar a linha, conforme o tamanho da palavra
    Já o segundo print irá printar o parametro
    Fora da função, o usuário interagiu com 3 frases armazenadas em f1, f2, f3
    Em seguida chamamos a função escreva() passando como parametro as frases
'''
