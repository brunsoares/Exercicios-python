#Quantidade de dias que foi alugado o carro
day = int(input('Quantos dias foi alugado o carro: '))
km = float(input('Quantos km foi rodado nesses dias: '))

#Calculos
preDay = day * 60
preKm = km * 0.15
preTotal = preDay + preKm

#mostrando
print('Com base nas informações dadas o preço do aluguel do carro é R${:.2f}\n'
      'Usado por {} dias e {}km\n'.format(preTotal, day, km))

'''
      O programa vai receber do usuário os dias e km rodados com o carro, armazenando nas respectivas variaveis
      Depois vem os cálculos: 
            ° preDay calcula o preço de cada dia (R$60 por dia) * os dias
            ° preKm calcula o preço do km rodado (R$0.15 por Km) * os km
            ° preTotal calcula o valor a ser pago pelo serviço, juntando preDay + preKm
      E depois printando na tela
'''
