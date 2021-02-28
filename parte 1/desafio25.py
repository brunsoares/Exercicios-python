#Nome da pessoa
nom = input('Digite seu nome completo: ')
nomUp = nom.title()
check = 'Silva' in nomUp
print('Seu nome é {}, e é {} para Silva'.format(nomUp, check))

'''
    Muito parecido com o exercicio passado, apenas a checagem muda para qualquer local da string
    O usuário digita uma string com seu nome e armazena em nom
    A variavel nomUp usa o title() para deixar cada primeira letra Maiuscula
    A variavel check funciona como a cidCheck na passada, pegando o valor 'Silva' e checando se existem em nomUp
    O print retornará se tem True ou False para Silva
'''
