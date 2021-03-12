#pegando a frase
frase = str(input('Digite uma frase: ')).strip() #tira espaços

#manipulando a frase
fraseLow = frase.lower()
#tirando todos os espaços
fraseNoSpc = fraseLow.replace(" ", "")
#print(fraseNoSpc)
#frase invertida
fraseInvt = fraseNoSpc[::-1]#fatia toda a frase, porem com passo invertido
#print(fraseInvt)

#verificação
if fraseInvt == fraseNoSpc:
    print('A palavra é um palindromo')
    print('{} -- é igual a -- {}'.format(fraseInvt, fraseNoSpc))
else:
    print('A palavra é normal apenas')
    print('{} -- é diferente de -- {}'.format(fraseInvt, fraseNoSpc))

'''
    Esse programa é para analisar se a palavra é um palindromo
    Primeiro pegamos uma frase do usuário, armazenado em frase
    Em seguida fazemos alterações para manipular a variavel frase
    Deixando em minusculo com o fraseLow, que usa o lower()
    Depois o fraseNoSpc, que tira o espaço usando o replace(), onde ele acha os espaços e troca por vazio
    E por fim o fraseInvt que inverte a frase usando o fatiamento, com o último parametro -1
    Na verificação se a fraseInvt for igual a fraseNoSpc, significa que é um palindromo
    Caso for False pro if irá pro else, onde é uma palavra normal
    Por fim ambos mostraram o print com as palavras
'''
