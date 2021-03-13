#lendo os valores
termo = int(input('Digite o termo da PA: '))
razao = int(input('Digite a razao da PA: '))
val = 10
limit = termo + (val - 1) * razao #val é a quant de valores mostrados, agora automatizado

while termo <= limit:
    print(termo, end=' -> ')

    if termo == limit: #chegou no ultimo termo
        print('Esse é o ultimo valor mostrado, você quer mostrar mais?\n')
        dec = int(input('Se deseja mostrar mais coloque quantos a mais, se não quiser coloque 0: '))
        if dec != 0:
            val = dec
            #print(val)
            limit = termo + val * razao

    termo += razao
print('Acabou')

'''
    Continuando o exercício passado, melhorando ele para o usuário continuar o programa se ele desejar
    O formato do começo continua o mesmo, porém foi adicionado uma variavel val que recebe 10, para definir o limite
    Dentro do while, temos a verificação caso o termo for igual a limit, sendo esse o último valor mostrado para o usuário
    Caso entre nessa verificação o usuário pode decidir se quer continuar ou não colocando outro valor, ou 0 para encerrar
    Esse valor armazenado em dec, caso dec for diferente de 0, val recebe dec e faz uma nova conta de limit
    Assim continuando o loop, por fim é mostrado o print encerrando o programa
'''
