import datetime

#Pegando o ano de nascimento do individuo
anoNas = int(input('Digite o ano de seu nascimento: '))
#pegando ano atual
anoAtu = datetime.date.today().year
#print(anoAtu)

#calculo
calc = anoAtu - anoNas
calMenor = 18 - calc
calMaior = calc - 18

#verificando
if calc < 18:
    print('Você ainda não vai se alistar pois fará {} anos esse ano e '
          'falta {} para você se alistar'.format(calc, calMenor))
elif calc == 18:
    print('Você precisará se alistar esse ano pois fará {} anos, ainda esse ano'.format(calc))
else:
    print('Você pode comemorar, não precisa se alistar pois fará {} anos esse ano e '
          'passou {} anos do alistamento'.format(calc, calMaior))

'''
    Programa para alistamento
    Primeiro importamos a biblioteca datetime para usar datas
    Depois o usuário vai digitar um valor para armazenar em anoNas
    A variavel anoAtu vai pegar o ano atual usando a função date.today().year do datetime
    Calculando a idade da pessoa, calc calculará o anoAtu menos o anoNas, dando a idade da pessoa
    A variavel calMenor vai calcular o tempo que falta para fazer 18, assim será 18 menor a idade (calc)
    Como também a calMaior que será o contrário, será a idade (calc) menos 18
    Na verificação se calc for menor que 18, entrará como menor de idade
    No elif é se a idade for igual a 18
    E caso caia no else, será que a pessoa já tem 18 anos
    Cada verificação tem um print mostrando resultados
'''
