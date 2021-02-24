#valor da tabuada
num = int(input('Digite um número e veja sua tabuada: '))

#fazendo manualmente
one = num * 1
two = num * 2
three = num * 3
four = num * 4
five = num * 5
six = num * 6
seven = num * 7
eight = num * 8
nine = num * 9
ten = num * 10

print('A tabuada do seu numéro {0} \n'
      '1 x {0} = {1} \n'
      '2 x {0} = {2} \n'
      '3 x {0} = {3} \n'
      '4 x {0} = {4} \n'
      '5 x {0} = {5} \n'
      '6 x {0} = {6} \n'
      '7 x {0} = {7} \n'
      '8 x {0} = {8} \n'
      '9 x {0} = {9} \n'
      '10 x {0} = {10} \n'
      'Acabou'.format(num, one, two, three, four, five, six, seven, eight, nine, ten))

'''
      O usuário vai digitar um valor, o programa vai pegar esse valor e em cada variavel
      Multiplicar por um valor de 1 - 10 (tabuada)
      Depois printado usando a formatação por indices {0}, onde o valor sempre será o format() no indice 0
      OBS: \n quebra a linha no print, usado para deixar organizado no console
'''
