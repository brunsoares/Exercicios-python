#Salario atual
salAtu = float(input('Qual o seu atual salário: '))
prom = salAtu * 0.15
salProm = salAtu + prom
print('Seu salário era de R${:.2f}, agora com a promoção R${:.2f}'.format(salAtu, salProm))

'''
    Bem parecido com o anterior
    O usuário vai digitar o valor do salario e sera armazenado em salAtu
    A variavel prom calcula a promoção adicional ao salário (15%)
    A variavel salProm calcula o salário atual + o valor da promoção
    E depois sai printado o resultado
'''
