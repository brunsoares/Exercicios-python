glr = []
dados = {}
listMul = []
listAcmId = []

totPess = 0
totIdad = 0

#loop infinito para pegar os valores de dados
while True:
    dados['Nome'] = str(input('Digite seu nome: ')).strip().title()
    dados['Idade'] = int(input('Digite sua idade: '))
    totIdad += dados['Idade']
    dados['Sexo'] = str(input('Digite seu sexo [F/M]: ')).strip().upper()
    totPess += 1
    # média de idade
    mdIdade = totIdad / totPess

    #lista acima da média
    if dados['Idade'] > mdIdade: #se a pessoa for maior que a média add na lista
        listAcmId.append(dados['Nome'])

    #lista com mulheres
    if dados['Sexo'] == 'F':
        #colocar na lista
        listMul.append(dados['Nome'])

    dec = str(input('Deseja continuar [S/N]: ')).strip().upper()
    glr.append(dados.copy()) #copia de dados para glr

    if dec != 'S':
        break


#print(glr)
print(f'Esse foi o total de pessoas cadastradas: {totPess}')
print(f'Essa é a média de idade do grupo: {mdIdade:.2f} anos')
print(f'Essa é a lista com todas as mulheres: {listMul}')
print(f'Essa é a lista com pessoas acima da média: {listAcmId}')

'''
    Programa que irá analisar informações de um grupo
    Primeiro criamos 1 dicionário vazio dados, e 3 listas vazias para armazenas verificações
    Além das 2 variaveis de controle zeradas
    Dentro do loop infinito, o usuário vai interagir pelo dados nos seguinte indices: nome, idade e sexo
    A variavel totIdade incrimenta a idade que o usuário colocar, e a totPess incrementa 1
    A variavel mdIdade vai calcular a média, usando o totIdade dividido pelo totPess
    Caso a idade for maior que a média, a listAcmId vai com append() adicionar o nome dessa pessoa
    Caso o sexo for feminino, listMul, com append() irá adicionar o nome da mulher adicionada
    Por fim temos a dec, onde o usuário vai decidir se continua ou não com o loop, resposta diferente de S loop para
    A lista glr com append() faz uma copia de dados com o copy()
    Por fim o print mostra todas as respostas das verificações
'''
