time = []
jog = {}
gols = []
totGols = 0
while True:
    jog['Nome do jogador'] = str(input('Digite o nome do jogador: ')).strip().title()
    jog['Total partidas'] = int(input('Quantas partidas jogou: '))

    #colocando o tanto de gols por partida
    for i in range(0, jog['Total partidas']):
        gols.append(int(input(f'Quantos gols na partida {i}: ')))
        jog['Gols por partida'] = gols[:]

    for g in gols:
        totGols += g
        jog['Total gols'] = totGols

    time.append(jog.copy())

    #limpeza
    gols.clear()
    jog.clear()
    totGols = 0

    #decisão de fechar cadastro
    dec = str(input('Deseja sair [S/N]: ')).strip().upper()
    if dec != 'S':
        break

#mostrando resultado
print('=*='*20)
print('{:<5}{:^30}{:>15}'.format('COD', 'Nome do jogador', 'Total de gols'))
for pos, i in enumerate(time):
    print(f'{pos:<5}{i["Nome do jogador"]:^30}{i["Total gols"]:>10}')

#print(time)

#Checando valores individuais
while True:
    print('\n\033[31m999 para a visualização dos detalhes\033[m\n')
    esc = int(input('Deseja ver detalhes de qual jogador, [COD]: '))
    if esc <= len(time)-1:#valores validos para ver os jogadores
        print(f'O jogador {time[esc]["Nome do jogador"]} fez em {time[esc]["Total partidas"]} jogos:\n'
              f'{time[esc]["Gols por partida"]} gols')
    if esc == 999:
        print('\033[31mADEUS...\033[m')
        break

'''
    Upgrade do exercício 93, com a possibilidade de ver detalhes do jogador
    Primeiro criamos um dicionário jog, 2 listas, todos vazios e uma variavel de controle totGols
    Dentro do loop infinito o usuário vai interagir com nome do jogador e total de partidas
    No loop for o i vai rodar sobre o limite de 0 ao total de partidas
    Cada loop gols vai com append() adicionar o valor, em seguida o jog no indice gols por partida vai fazer uma copia de gols
    Em seguida entra no loop onde g irá rodar sobre gols
    O totGols irá incrementar o valor de g, e jog no indice total gols irá receber totGols
    A lista time pega com append() uma copia de jog pelo copy()
    Em seguida limpamos as variaveis, gols e jog pelo clear() e zerando a totGols
    Por fim temos a interação caso o usuário deseje fechar o loop
    Em seguida temos os prints com as respostas, assim tem um loop que roda para mostrar todos os jogadores
    Agora para visualizar os detalhes, dentro do loop infinito o usuário vai interagir com o esc, colocando o código do jogador
    Caso o esc for menor ou igual ao tamanho de time menos 1, ele irá mostrar o jogador com esse código válido
    Caso o esc for igual a 999, o loop será fechado e o programa encerrado
'''
