#calculando o tamanho da parede
width = float(input('Qual a largura da parede em metros: '))
height = float(input('Qual a altura da parede em metros: '))
area = width * height
tint = area / 2 #um litro pinta 2m² de area, ou seja 20 de area 10 litros de tinta
print('A parede contém {}m² de área, portanto será necessário {}L de tinta'.format(area, tint))
print('OBS: Baseando-se que a tinta por litro pinta 2m²')

'''
    As variaveis width e height recebem os valores do usuário
    Depois a variavel area calcula a área com base no width e height e armazena o valor
    A variavel tint pega esse valor da area e divide por 2 para  saber quanta tinta consegue pintar
    E depois é mostrado no print a área e quanto de tinta vai necessitar
'''
