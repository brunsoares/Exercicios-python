import math

#pegando angulo
ang = float(input('Digite um angulo qualquer: '))
#conversão do angulo do numero para radianos
num = math.radians(ang)
#Mostrando info
sen = math.sin(num)
cos = math.cos(num)
tang = math.tan(num)

print('Seno do angulo {} é {:.2f}'.format(ang, sen))
print('Coseno do angulo {} é {:.2f}'.format(ang, cos))
print('Tangente do angulo {} é {:.2f}'.format(ang, tang))

'''
    Nesse programa precisa achar informações de um ângulo
    Primeiro importa a biblioteca math
    Depois a variavel ang armazena um valor float do usuário
    Esse mesmo valor é convertido para randianos pelo num que usa a função radians() do math
    Em seguida as variaveis sen, cos, tang usa funções do math (sin, cos, tan) para achar respectivamente seus valores
    Depois o printa mostra as informações dessas variaveis
'''
