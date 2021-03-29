from datetime import date

pessoa = {}

pessoa['Nome'] = str(input('Digite seu nome: ')).strip().title()
#pegando idade
anoAtu = date.today().year
anoNasc = int(input('Digite o ano de nascimento: '))
idade = anoAtu - anoNasc
pessoa['Idade'] = idade
#numero da carteira de trabalho, não interessa, so importa se for diferente de 0
pessoa['Carteira de Trabalho'] = int(input('Digite o número da carteira de trabalho: '))

if pessoa['Carteira de Trabalho'] != 0:
    pessoa['Ano de Contratação'] = int(input('Digite o ano de contratação: '))
    pessoa['Salário'] = float(input('Digite o valor do salário: '))
    #descobrindo a idade de aposentadoria
    #idade contratada + 35 anos que é o limite do exercicio
    idadeCont = pessoa['Ano de Contratação'] - anoNasc
    apos = idadeCont + 35
    pessoa['Aposentar'] = apos

print('=*='*20)

print(f'O nome da pessoa é: {pessoa["Nome"]}\n'
      f'Ela tem: {pessoa["Idade"]} anos\n'
      f'N° da carteira de trabalho (0 não tem): {pessoa["Carteira de Trabalho"]}')

if pessoa['Carteira de Trabalho'] != 0:
    print(f'Ano de contratação: {pessoa["Ano de Contratação"]}\n'
          f'Salário de R${pessoa["Salário"]}\n'
          f'Vai se aposentar com: {pessoa["Aposentar"]} anos')

'''
    Programa que irá analisar os dados de uma pessoa
    Primeiro importamos date de datetime, e criamos um dicionário vazio, pessoa
    Primeira interação será o nome no indice pessoa['nome']
    Em seguida pegamos o ano atual pelo date.today().year(), armazenado em anoAtu
    E o usuário fornece seu ano de nascimento armazenado em anoNasc
    A variavel idade pega o anoAtu menos o anoNasc, e armazena no pessoa['idade'] esse valor
    Para o indice da carteira de trabalho, o usuário vai digitar o número da carteira
    Caso esse valor for diferente de 0, ele tem carteira e assim surgirá essas interações:
    -O ano de contratação e o salário
    Assim a variavel idadeCont pega o ano da contratação menos o anoNasc, sabendo com quantos anos foi contratada
    A variavel apos vai calcular a aposentadoria com o valor da idadeCont mais 35 anos, assim armazenando no indice aposentar
    Depois  aparece dois tipos de print, primeiro padrão com as informações, e caso a carteira seja diferente de zero
    Será mostrado os dados do trabalho como ano de contrato, salário e aposentar
'''
