#Criando a lista do brasileirao 2020/2021
times = ('Internacional', 'Atlético Mineiro', 'Flamengo',
         'São Paulo', 'Fluminense', 'Palmeiras',
         'Grêmio', 'Athletico-PR', 'Ceará',
         'Corinthians', 'Santos', 'Atlético Goianiense',
         'Bragantino', 'Vasco da Gama', 'Bahia',
         'Sport Recife', 'Fortaleza', 'Goiás',
         'Coritiba', 'Botafogo')
#print(len(times))

#pegando interação (bonus)
usu = str(input('Você quer ver informações do \033[32mBrasileirão\033[m: [S/N] ')).strip().upper()

if usu == 'S':
    #Manipulando a tupla
    fiveTms = print(f'\nEsses são os 5° primeiros colocados: {times[:5]}\n')
    ultTms = print(f'\nEsses são os 4 últimos times da tabela, prontos para rebaixamento: {times[-4:]}\n')
    alpTms = print('\nTimes por ordem alfabética:\n{}\n'.format(sorted(times)))
    #pegando posição do time do palmeiras
    #No index foi colocado +1 pois começa na posição 0 a tupla
    palPos = print(f'\nO Palmeiras está na posição: {times.index("Palmeiras")+1}')
else:
    print('Fica sem informação do futebol então, \033[31mTCHAU\033[m')

'''
    Programa que mostra informações sobre o futebol
    Primeiro criamos uma tupla manualmente, com todos os times do campeonato
    Em seguida a variavel usu armazena a interação com usuário que decide se quer ver informações do futebol ou não
    Caso ele queira [S] cai no if onde é mostrado as informações por essa ordem:
        -fiveTms = os primeiros 5 times, usando fatiamento de string [:5]
        -ultTms = os últimos 4 times, também usando fatiamento, porém ao contrário [-4:]
        -alpTms = que mostra todos os time por ordem alfabética usando a função sorted()
        -palPos = posição do time do Palmeiras, onde usa uma função dentro de tuplas, index() para procurar 'Palmeiras'
    Caso o usuário não deseje ver as informações o programa cai no else, onde apenas mostra um print finalizando o programa
'''
