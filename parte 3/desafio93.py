jog = {}

#pegando dados
jog['Nome do jogador'] = str(input('Digite o nome do jogador: ')).strip().title()
jog['Total partidas'] = int(input('Quantas partidas jogou: '))

#lista de gol
gols = []

#Quantos gols em cada partida
for i in range(0, jog['Total partidas']):
    gols.append(int(input(f'Quantos gols na partida {i}°: ')))

#total de gol
totGols = 0
for g in gols:
    totGols += g
#print(totGols)

#adicionando dicionario
jog['Total gols'] = totGols
jog['Gols em partidas'] = gols
#print(jog)

#Mostrando resultados
print(f'O jogador: {jog["Nome do jogador"]}, jogou {jog["Total partidas"]} partidas e '
      f'marcou ao todo no campeonato {jog["Total gols"]} gols')
print('Partidas:')
for pos, v in enumerate(gols):
    print(f'Partida {pos}: {v} gols')

'''
    Esse programa vai analisar informações de um jogador
    Primeiro criamos um dicionário vazio, jog, e pedimos interações ao usuário como nome e total de partidas
    É criado uma lista vazia chamada gols, e assim entra no loop for para saber quantos gols em cada partida, usando o limite de 0 e o valor de total de partidas
    Para cada loop a lista gols da append() no valor
    Assim é criado uma variavel de controle totGols zerada, e dentro do loop for, onde g iria rodar sobre gols
    Onde totGols iria incrimentar g, somando todos os gols
    Em seguida adicionamos ao dicionário, com o indice total de gols e gols em partidas, pelo totGols e gols respectivamente
    No print será mostrado os resultados, e por fim um loop com pos e v rodando sobre o enumarete() de gols para mostrar cada gols nas partidas
'''
