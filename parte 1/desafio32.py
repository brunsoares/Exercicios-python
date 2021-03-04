#Pegando o ano do usuario
anoUsu = int(input('Digite um ano qualquer: '))

#vendo se ele é bissexto
if anoUsu % 4 == 0 and anoUsu % 100 != 0 or anoUsu % 400 == 0:
#o calculo do ano bissexto é que se for divisivel por 4 e restar 0 é bissexto
#porém tem a excessão que anos multiplos de 100 e não divisiveis por 400 não sao bissextos
    print('{} é um ano bissexto, eita ;-;'.format(anoUsu))
else:
    print('{} não é um ano bissexto, hehe'.format(anoUsu))

'''
    Programa para checar se o ano é bissexto ou não
    Primeiro pegamos o ano do usuário, armazenado em anoUsu
    A verificação usa varias etapas, primeiro:
        -Se o anoUsu dividido por 4 restar 0
        -Também não pode ser multiplo de 100, assim anoUsu dividido por 100 não restar 0 (!=)
        -Ou se o anoUsu dividido por 400 restar 0
    Esse if tem varias condições para ser verdadeiro, usando operadores como o AND e OR
    Em seguida caso for True a condição, mostrará o ano e a mensagem mostrando que é ano bissexto
    Caso for False, entra no else, que apenas mostrará que o ano não é bissexto
'''
