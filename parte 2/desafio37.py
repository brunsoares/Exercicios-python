from time import sleep

#Pegando o valor do usuario
valUsu = int(input('Digite um valor para a conversão: '))
print('Escolha um meio de conversão:\n'
      '1 para binário\n'
      '2 para octal\n'
      '3 para hexadecimal')
esco = int(input('Qual meio desejado: '))

#Calculando binario
bina = bin(valUsu)
#print(bina)

#Calculando octal
oc = oct(valUsu)
#print(oc)

#Calculando hexadecimal
hx = hex(valUsu)
#print(hx)

#Verificando a conversão escolhida
if esco == 1:
    print('Você escolheu binário, aguarde o processamento da resposta')
    print('PROCESSANDO...')
    sleep(2)
    print('O valor em binário é = \033[32m{}'.format(bina))

elif esco == 2:
    print('Você escolheu octal, aguarde o processamento da resposta')
    print('PROCESSANDO...')
    sleep(2)
    print('O valor em octal é = \033[32m{}'.format(oc))
elif esco == 3:
    print('Você escolheu hexadecimal, aguarde o processamento da resposta')
    print('PROCESSANDO...')
    sleep(2)
    print('O valor em hexadecimal é = \033[32m{}'.format(hx))
else:
    print('Número inválido, por padrão será usado binário')
    print('PROCESSANDO...')
    sleep(2)
    print('O valor em binário é = \033[32m{}'.format(bina))

'''
    Esse é um programa mais complexo, utilizando menus
    Primeiro importamos a biblioteca time para usar o sleep()
    O usuário vai digitar um valor armazenado em valUsu, valor esse que será usado para conversão de números
    Depois vai mostrar um print mostrando as opções do usuário
    E depois o usuário vai digitar sua opção que será armazenado em esco
    Com os dados de valUsu começa o as conversões, primeiro com a variavel bina que converterá para binário o número do usuario pela função padrão bin()
    Depois temos a variavel oc que armazenará a conversão pra octal feita pela função oct(), e por fim o hx que armazenará a conversão em hexadecimal pela função hex()
    Agora colocando a verificação que funcionará com base na escolha do usuário no menu
    Assim se ele colocou 1 a condição será binário, 2 será octal, 3 hexadecimal
    Todas as condições tem o sleep() para deixar mais agradavel o programa
    OBS: Caso o usuário escolher um número inválido, por padrão será binário
'''
