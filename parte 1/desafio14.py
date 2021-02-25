#Pegando a temperatura em celsius
c = float(input('Qual a temperatura em °C: '))
#convertendo para fahrenheit
f = (c * 9 / 5) + 32
print('A temperatura {}°C equivale a {}°F'.format(c, f))

'''
    A variavel c vai receber uma temperatura (Usamos o Celsius) como base
    A variavel f vai converter usando a fórmula para conversão
    E depois é printado na tela cada valor
'''
