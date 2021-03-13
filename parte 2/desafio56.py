somaId = 0
maiorId = 0
nomeDoHomVeio = ''
quantFemea = 0
#pegando informaçoes usuario
for i in range(1, 5):
    print('----- {}ª Pessoa -----'.format(i))
    nom = str(input('Digite seu nome: ')).strip().title()
    ida = int(input('Digite sua idade: '))
    sex = str(input('Qual seu sexo [M/F]: ')).upper()

    somaId += ida

    #Fazendo o nome do homem mais velho
    if i == 1: #Sendo a primeira pessoa, ele é mais velho pois não tem outros dados a comparar
        maiorId = ida
        nomeDoHomVeio = nom
    else:#Aqui eh para quando tiver outros dados a comparar
        if ida > maiorId and sex == 'M': #Quando tiver um M (HOMEM) mais velho trocar os dados
            maiorId = ida
            nomeDoHomVeio = nom

    #Vendo quantas mulheres tem menos de 20 anos
    if sex == 'F' and ida < 20:
        quantFemea += 1

#fazendo a media de idade
md = somaId / 4
print('A média de idade do grupo é igual a {} anos'.format(md))
print('O nome do Homem mais velho é {} com {} anos'.format(nomeDoHomVeio, maiorId))
print('A quantidade de mulheres com menos de 20 anos é {}'.format(quantFemea))

'''
    Esse programa irá analisar dados de um grupo de pessoas
    Primeiro criamos 3 variaveis de controles com valor inicial de 0, e a variavel nomDoHomVeio = '' para acrescentar depois
    Assim entramos no loop para começar a pegar a informação dos usuários
    O for irá rodar i 4 vezes
    Primeiro pegamos os dados, como nome, idade e sexo, armazenados respectivamente 
    A primeira variavel de controle usada é a somaId que irá acrescentar a idade dos usuários
    Agora nas verificações para checar o nome do homem mais velho
    Caso o i seja igual a 1, significa que é a primeira pessoa do loop, assim a maiorId recebe a idade e o nomeDoHomVeio recebe nom
    Caso saia da verificação do i, cairá no else, ou seja, outras pessoas no loop
    Assim entra uma verificação para ver se é homem a pessoa e se a idade atual (ida) é maior que maiorId (idade primária)
    Caso seja True, a maiorId recebe a idade atual do homem e nomeDoHomVeio recebe o seu nome
    Por fim tem uma verificação para saber quantidade de mulheres com mais de 20 anos
    Assim se o sexo for igual feminino ('F') e a ida for maior que 20, entra na condição, onde a variavel de controle acrescenta 1 na contagem de mulheres
    Em seguida fazemos a média de idade do grupo, na variavel md, onde pega o somaId de todos e divide pela quantidade de pessoas
    Após isso é printado todos os valores e suas verificações
'''
