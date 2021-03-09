#Aprimorando exercicio 35
#Pegando valores do usuario
rt1 = float(input('Digite o valor para a primeira reta: '))
rt2 = float(input('Digite o valor para a segunda reta: '))
rt3 = float(input('Digite o valor para a terceira reta: '))

#calculos
calRt1 = rt1 < (rt2 + rt3)
calRt2 = rt2 < (rt1 + rt3)
calRt3 = rt3 < (rt1 + rt2)

if calRt1 == True and calRt2 == True and calRt3 == True:
    print('Dada as informações é possivel fazer um triangulo')
    acao = input('-*-Aperte enter para ver o tipo do triangulo que pode ser feito-*-')
    if acao == '':
        if rt1 == rt2 and rt1 == rt3:
            #Lados iguais triangulo equilatero
            print('O seu triangulo é o \033[1;32mEQUILÁTERO')
        elif rt1 == rt2 and rt1 != rt3 or rt1 == rt3 and rt1 != rt2 or rt2 == rt3 and rt2 != rt1:
            print('O seu triangulo é o \033[1;36mISÓSCELES')
        else:
            print('O seu triangulo é o \033[1;35mESCALENO')
else:
    print('Reveja as informações dadas para formar um triangulo')

'''
    Esse é o primeiro exercício de aprimoramento, no caso aprimoramento do exercício 35
    Primeiro o programa vai agir como o exercício 35
    O que foi aprimorado foi a verificação, onde após formar um triângulo, o usuário pode apertar Enter para ver informações
    Seguindo a partir do outro programa, a variavel acao é um input para o usuário  digitar enter, no caso vazio ''
    Se ele digitou '', entrará na condição True, e assim se todas as retas forem iguais, cai na primeira verificação
    Caso alguma reta seja diferente das demais, cai no elif
    E caso não nenhuma bata entra no else
    Cada verificação mostra o tipo de triângulo apropriado
'''
