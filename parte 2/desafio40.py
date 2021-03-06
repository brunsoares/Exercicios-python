#pegando nota do aluno
not1 = float(input('Digite a primeira nota: '))
not2 = float(input('Digite a segunda nota: '))

#media
md = (not1 + not2) / 2

#verificação
if md < 5:
    print('Você está reprovado esse ano, T R I S T E')
    print('Média = {:.1f}'.format(md))
elif md >= 5 and md <= 6.9:
    print('Você está de recuperação esse ano, E S T U D E')
    print('Média = {:.1f}'.format(md))
else:
    print('Você foi aprovado meus parabéns, P A R A B É N S')
    print('Média = {:.1f}'.format(md))

'''
    Programa para verificar média
    Primeiro o usuário vai digitar duas notas, armazenadas em not1 e not2
    A variavel md vai pegar a soma das notas e dividir por 2
    Na verificação se a md for menor que 5 o aluno está reprovado
    Caso caia no elif o aluno está de recuperação, com uma média entre 5 e 6.9
    E caso caia no else, o aluno passou com mais de 7 de média
'''
