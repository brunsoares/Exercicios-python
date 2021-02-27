import math

#pegando cateto oposto (a²) e o cateto adjacente (b²)
catOp = float(input('Digite o valor do cateto oposto: '))
catAd = float(input('Digite o valor do cateto adjacente: '))

#Calculos formula = a²+b²=c² #ou seja c é a raiz quadrada da soma dos catetos
a2 = math.pow(catOp, 2)
b2 = math.pow(catAd, 2)
#hipotenusa (c²)
som = a2 + b2
c2 = math.sqrt(som)

#forma facilitada pelo math
hip = math.hypot(catOp, catAd)

print('A hipotenusa vai medir {:.2f}'.format(c2))
print('A hipotenusa mediu {:.2f}, usando a função do math, hypot()'.format(hip))

'''
    Nesse exercicio é demonstrado de duas formas como achar a hipotenusa
    Usamos novamente a import math para usar calculos mais avançados
    ! A Primeira forma é manual: a variavel catOp, e catAd recebem um float do usuário
    Depois as variaveis a2 e b2 pegam o valor de catOp / catAd e com a função pow() usa potência no número 2
    A variavel som vai somar valores de a2 e b2
    E a variavel c2 vai pegar som e achar sua raiz quadrada pela função sqrt()
    ! A segunda forma é automatica: a variavel hip vai usar a função hypot(), que apenas precisa do cateto oposto e adjacente
    E automaticamente acha a hipotenusa
    Logo após as duas formas, o printa mostra o resultado de ambas
'''
