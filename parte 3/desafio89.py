#lendo as notas no loop
sala = []
contAlun = 0
while True:
    nome = str(input('Digite o nome do aluno: ')).strip().title()
    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segunda nota: '))

    #media
    media = (nota1 + nota2) / 2
    sala.append([nome, [nota1, nota2], media]) #formato da lista sala

    contAlun += 1
    dec = str(input('Deseja continuar [S/N]: ')).strip().upper()
    if dec != 'S':
        print('\033[31mFechamento de notas da turma, aguarde\033[m')
        break


print('=*='*20)
print('{:^60}'.format('Boletim'))
print('=*='*20)
print('{:^20}{:^20}{:^20}'.format('n°', 'Nome', 'Média'))
for pos, i in enumerate(sala):
    print(f'{pos:^20}{i[0]:^20}{i[2]:^20.1f}')

while True:
    dec = int(input('Digite o número do aluno para ver as notas separadas (999 para): '))
    if dec <= len(sala)-1:#valores validos ao teste
        print(f'A nota do aluno {sala[dec][0]} foi: {sala[dec][1]}')
    else:
        print('Adeus...')
        break

'''
    Programa de leitura de notas
    Primeiro criamos a sala lista vazia e uma variavel de controle zerada, contAlun
    Dentro do loop infinito, o usuário interage colocando o nome e as notas do aluno
    Em seguida é calculado a média armazenado em media, e a sala da append() em todos os valores
    O contAlun incrementa 1 e o usuário interage em dec, caso dec for diferente de S loop encerra
    Por fim é mostrado o boletim dos alunos, personalizado, for é apenas para rodar sobre os valores da lista (sala) e printar os valores
    Dentro do loop infinito, o usuário interage novamente em dec decidindo o número do aluno que irá ver as notas separadas
    Caso a dec for menor que o tamanho da sala - 1, irá printar as notas do aluno, pelo código dele
    Caso contrário encerrará o programa 
'''
