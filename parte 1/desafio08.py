#Valor em metros
m = float(input('Digite o número em metros: '))
km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10
cm = m * 100
mm = m * 1000
print('O valor digitado é {}m, em decímetro é {}dm, em centimetros é {}cm, e em milimetros é {}mm'.format(m, dm, cm, mm))
print('Agora em decametro é {}dam, em hectometro é {}hm, por fim em quilometros é {}km'.format(dam, hm, km))
'''
    O usuário vai digitar um valor float
    E esse mesmo valor vai ser convertido e armazenado em cada uma das variaveis
    Depois printado pelos dois prints
'''
