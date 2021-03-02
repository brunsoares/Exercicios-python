#Pegando a velocidade da pessoa
velo = int(input('Digite a velocidade do carro: '))

if velo > 80:
    print('Você ultrapassou o limite de velocidade, passou a {}km/h na pista a 80km/h'.format(velo))
    valMult = (velo - 80) * 7 #7 valor da multa por km a mais
    print('Você vai receber uma multa no valor de R${:.2f}'.format(valMult))
else:
    print('Você passou a {}km/h continue a viagem'.format(velo))

'''
    Nesse programa simula um radar básico, primeiro o usuário digita um valor armazenado em velo
    Na verificação, se (if) a velo for maior que 80 (limite fictício), vai mostrar que ultrapassou o limite
    E se cair nessa verificação, vai calcular uma multa, a partir do valMult, que vai calcular prieiro a velocidade do carro menos 80 (limite), e em seguida multiplicar por 7, valor por km
    E depois printar esse valor
    Caso a verificação seja False, ou seja não caiu no if, o else vai mostrar a velocidade no print apenas
'''
