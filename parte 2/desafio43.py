#Pegando valores do usuario
valAlt = float(input('Digite sua altura em metros: '))
valPes = float(input('Digite seu peso em kg: '))

#calculo
imc = valPes / (valAlt ** 2)

if imc < 18.5:
    print('Seu imc está em {:.2f}, classificado como: \033[1;31mABAIXO DO PESO'.format(imc))
elif imc >= 18.5 and imc <= 25:
    print('Seu imc está em {:.2f}, classificado como: \033[1;32mPESO IDEAL'.format(imc))
elif imc > 25 and imc < 30:
    print('Seu imc está em {:.2f}, classificado como: \033[1;36mSOBREPESO'.format(imc))
elif imc >= 30 and imc <= 40:
    print('Seu imc está em {:.2f}, classificado como: \033[1;34mOBESIDADE'.format(imc))
else:
    print('Seu imc está em {:.2f}, classificado como: \033[1;35mOBESIDADE MÓRBIDA'.format(imc))

'''
    Esse programa calcula o imc de uma pessoa, mostrando qual sua classificação
    Primeiro o usuário vai digitar a altura (valAlt) e o peso (valPes)
    Assim o imc vai ser calculado pela divisão do peso pela altura elevado a 2
    Nas verificações, caso o imc for menor que 18.5, cairá na primeira verificação
    Caso for False na primeira pode entrar nos elif, o primeiro está entre maior ou igual a 18.5 e menor ou igual a 25
    O segundo está entre maior que 25 e menor que 30
    O último elif está entre maior ou igual a 30, e menor ou igual a 40
    Caso não bata em nenhuma, cairá no else assim acima de 40 o imc
    Cada verificação mostra a classificação e seu imc
'''
