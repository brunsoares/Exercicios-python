#pegando valores
valProd = float(input('Digite o valor do produto selecionado: R$'))
print('Formas de pagamentos aceitas:\n'
      '1 para dinheiro / cheque a vista\n'
      '2 para cartão a vista\n'
      '3 para cartão parcelado x2\n'
      '4 para cartão parcelado x3 ou mais')
formPag = int(input('Digite a forma de pagamento desejada: '))

#calculando descontos
#dinheiro
calDin = valProd * 0.10
precDin = valProd - calDin
#print(precDin)

#cartao vista
calCartVist = valProd * 0.05
precCartVist = valProd - calCartVist
#print(precCartVist)

#cartao x2
precCartX2 = valProd
#print(precCartX2)

#cartao x3
calCartX3 = valProd * 0.20
precCartX3 = valProd + calCartX3
#print(precCartX3)

#condições e verificacao
if formPag == 1:
    #Dinheiro ou cheque
    print('O meio escolhido foi Dinheiro ou cheque a vista, o preço do produto ficou em '
          'R${:.2f}, boas compras'.format(precDin))
elif formPag == 2:
    #cartao a vista
    print('O meio escolhido foi Cartão a vista, o preço do produto ficou em '
          'R${:.2f}, boas compras'.format(precCartVist))
elif formPag == 3:
    #Cartão x2
    print('O meio escolhido foi Cartão x2, o preço do produto ficou em '
          'R${:.2f}, boas compras'.format(precCartX2))
elif formPag == 4:
    #cartão x3
    print('O meio escolhido foi Cartão x3, o preço do produto ficou em '
          'R${:.2f}, com juros, boas compras'.format(precCartX3))
else:
    #esquema anti burrice do usuario
    print('O meio escolhido foi inválido, por padrão foi colocado dinheiro ou cheque a vista \n'
          'Preço do produto ficou em R${:.2f}, boas compras'.format(precDin))


'''
    Programa de menu para pagamento de lojas
    Primeiro o usuário digita o valor do produto, armazenado em valProd, em seguida aparece um menu com indices demonstrando qual valor preencher
    E depois pergunta qual forma de pagamento do menu o cliente quer, cada uma tem suas caracteristicas
    Após isso temos o calculo das formas de pagamento, cada uma tem caracteristicas de desconto ou acrescimo
    Com isso vamos para verificação, pela forma de pagamento selecionada, no primeiro caso é o 1 (dinheiro)
    Depois cairá nos elif dependendo da forma de pagamento
    Caso a forma for inválido, entra no else onde mostrá inválido e usa dinheiro como padrão
    Cada caso mostrará o valor da forma de pagamento, e a forma de pagamento selecionada
'''
