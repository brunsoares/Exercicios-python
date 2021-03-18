print('\033[31mATENÇÃO, apenas temos cédulas de R$50, R$20, R$10,R$1\033[m')
val = int(input('Digite o valor a ser sacado: R$'))
total = val
ced = 50 #cedula primaria
quntCed = 0 #quantidade de cedula

while True:
    if total >= ced: #se o total for maior que a ced, então reduza essa cedula ao maximo do total
        total -= ced
        quntCed += 1 #uma cedula foi usada
    else: #total já é menor que a cedula atual, trocar a cedula
        #so vai printar as cedulas usadas
        if quntCed > 0:
            print(f'Foi usado {quntCed} cédulas, no valor de R${ced}')
        if ced == 50: #se for de 50 troca para a de 20
            ced = 20
        elif ced == 20: # 20 para a de 10
            ced = 10
        elif ced == 10: #10 para a de 1
            ced = 1
        quntCed = 0 #resetando a quant de cedula na hora da troca

        #fim do programa
        if total == 0:
            print('Acabou a impressão de cedúlas')
            break

'''
    Programa para simulação de caixa eletrônico
    Primeiro pegamos valores do usuário, como a quantidade de ele deseja retirar, armazenado em val
    Depois passamos para a variavel total o valor de val
    Adicionamos valores a variavel ced como cédula principal de 50, e quntCed zerada para controle
    Dentro do loop infinito, se o total for maior ou igual a ced, ou seja consegue pagar com a cédula de 50
    O total é diminuido pelo valor da ced, e quntCed incrementa 1 cada vez que essa verificação bater
    Caso o total for menor que a cédula de 50, entra no else, assim usando outras notas
    A primeira verificação é caso a quntCed for maior que zero, para mostrar quantas cédulas e quais foram usadas até o momento
    Assim usamos a troca de cédula, diminuindo conforme o total diminui, de 50 para 20, de 20 para 10 e de 10 para 1
    Por fim sempre reseta a quantidade de cédula usada para a troca de cédulas
    Caso o total for igual a 0, significa que acabou o valor e as notas foram emitidas, assim printando que acabou o valor e dando um break no loop
'''
