glr = []
dados = []
#variaveis de verificação
ctnPess = 0
pesado = 0
leve = 0
while True:
    dados.append(str(input('Digite seu nome: ')).strip().title())
    dados.append(float(input('Digite seu peso: ')))
    ctnPess += 1
    dec = str(input('Deseja continua [S/N]: ')).strip().upper()
    #glrPesada verificação
    if ctnPess == 1: #primeira pessoas
        pesado = dados[1]
        leve = dados[1]
    elif ctnPess != 1: #outras pessoas
        if pesado <= dados[1]:
            pesado = dados[1]
        if leve >= dados[1]:
            leve = dados[1]
    # colocando na lista
    glr.append(dados[:])  # criando COPIA
    dados.clear()
    #parando programa
    if dec != 'S':
        print('\033[31mFINALIZANDO PROGRAMA...\033[m')
        break


print(f'{ctnPess} pessoas foram cadastradas')
#print(f'{pesado}, {leve}')
print(f'Pessoas pesadas, com {pesado}Kg => ', end="")
for i in glr:
    if i[1] == pesado:
        print(i[0], end=", ")
print(f'\nPessoas leves, com {leve}Kg => ', end="")
for i in glr:
    if i[1] == leve:
        print(i[0], end=", ")

'''
    Programa irá analisar o peso de um grupo de usuários
    Primeiro criamos 2 listas vazias, glr e dados, e depois 3 variaveis de controle zeradas
    Dentro do loop infinito, dados vai dar append() em duas interações com o usuário, nome e peso
    A variavel ctnPess incrementa 1, e o usuário interage com o dec, caso dec diferente de S o loop é encerrado
    Caso o ctnPess for igual a 1, é a primeira pessoa, então pesado e leve pegam o mesmo dado, na posição 1 que é o peso da pessoa
    Caso não seja a primeira pessoa entra em outra verificação, caso pesado for menor que dados[1], pesado recebe esse novo peso
    E caso leve for maior que dados[1], leve irá receber esse novo peso
    E para essa verificação funcionar criamos uma copia desses dados em glr, e em seguida limpamos dados com o clear()
    Os resultados mostram primeiro a quantidade de pessoas cadastradas
    Depois as pessoas com pesado, seguido por um loop que o i roda sobre o pesado e acha a pessoa com esse peso
    O mesmo ocorre com o leve, seguido pelo loop onde o i roda sobre o leve e acha o nome da pessoa com esse peso
'''
