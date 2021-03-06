#Programa de financiamento de uma casa
#pegando informações
valCasa = float(input('Digite o valor da casa desejada: R$'))
valSalar = float(input('Digite o valor do seu salário: R$'))
quantAno = int(input('Digite o tempo em anos para pagar essa casa: '))

#calculando a prestação mensal
prestMensal = valCasa / (quantAno * 12) #vezes 12 para saber a quantidade de meses
#limite da prestação = até 30% do salario
limit = valSalar * 0.30
#print(prestMensal)
#print(limit)

#Verificação
if prestMensal > limit:
    print('O valor mensal ultrapassa o limite do seu salário, financiamento negado')
else:
    print('O valor mensal está dentro do seu limite, a prestação mensal sairá R${:.2f}, '
          'financiamento aprovado'.format(prestMensal))

'''
    Para esse programa o usuário vai digitar valores para ser armazenado em valCasa, valSalar, quantAno
    Após armazenados a variavel prestMensal vai pegar o valCasa e dividir pela (quantAno * 12), isso para saber a quantidade de meses
    A variavel limit é para usar como limite de prestação válidas, 30% do salário
    A verificação coloca a prestMensal se for maior que o limit, assim a pessoa não pode fazer o financiamento pois o valor da prestação mensal ultrapassou o limite
    Caso der False e cair no else, o financiamento foi aprovado assim mostrará os resultados
'''
