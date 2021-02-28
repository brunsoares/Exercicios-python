#pegando nome da cidade
cid = str(input('Digite o nome da sua cidade: ')).strip() #tirando espaços inuteis

#deixando em maiusculo para evitar erros
cidUp = cid.capitalize()

#Dividindo
cidDiv = cidUp.split()

#checagem
cidCheck = 'Santo' in cidDiv[0]

print('A sua cidade começa com nome "Santo" ? {}'.format(cidCheck))

'''
    O usuário vai digitar o nome da cidade armazenado em cid, e o programa vai ver se tem Santo como primeiro nome ou não
    Primeiro usa o cidUp para deixar capitalizado o nome das cidades
    E cidDiv para fazer a divisão em uma lista
    A checagem é feita pela cidCheck que pega a palavra 'Santo' e vê se está em cidDiv[0] (primeiro valor da lista)
    Isso irá retornar True (caso for verdade) e False (caso for falso)
    O print mostrará a resposta ao usuário
'''
