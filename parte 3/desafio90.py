nots = {}

nots['nome'] = str(input('Digite o nome do aluno: ')).strip().title()
nots['média'] = float(input('Digite a média do aluno: '))

if nots['média'] < 7:
    #print('Reprovado')
    nots['situação'] = '\033[31mReprovado!\033[m'
else:
    #print('Aprovado')
    nots['situação'] = '\033[32mAprovado!\033[m'

print(f'O aluno {nots["nome"]} está com uma média de {nots["média"]}, por isso está {nots["situação"]}')

'''
    Primeiro exercício usando dicionários, onde será usado outra forma para verificar notas
    Primeiro criamos um dicionário vazio nots 
    OBS: a principal mudança de dicionários para as outras (tupla e lista) é que seus indices podem ser modificados, não sendo númericos
    Assim pegamos duas interações do usuário, em nots no indice nome, e no indice média
    Caso a nots no indice média for menor que 7 será, adicionado uma nots indice situação como reprovado
    Caso for maior ou igual a 7 esse nots situação será aprovado
    Por fim é mostrado o resultado usando nots e seus diversos indices
'''
