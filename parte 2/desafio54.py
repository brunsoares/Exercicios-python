import datetime

#ano atual
anoAtu = datetime.date.today().year
pessMaior = 0
pessMenor = 0
#Pegando ano de nascimento das pessoas
for a in range(0, 7):
    ano = int(input('Digite o ano de seu nascimento: '))
    calc = anoAtu - ano
    #print(calc)
    if calc < 21:
        pessMenor += 1
        print('Essa pessoa ainda é menor de idade e tem {} anos'.format(calc))
    else:
        pessMaior += 1
        print('Essa pessoa já é maior de idade e tem {} anos'.format(calc))

print('Dessas pessoas, {} atingiram 21 anos completos'.format(pessMaior))
print('Dessas outras pessoas, {} ainda são crianças hehe'.format(pessMenor))

'''
    Esse programa iremos ver a quantidade de pessoas maiores de idade e menores de idade
    Primeiro importamos a biblioteca datetime
    Usamos a datetime na variavel anoAtu, onde pegamos o ano atual pelo date.today().year
    Depois criamos duas variaveis com valor 0, para ser acrescentado depois, a pessMaior e pessMenor
    Assim entramos no loop onde o a irá rodar 7 vezes
    Dentro do loop o usuário vai digitar o ano de nascimento, armazenado em ano
    A variavel calc irá calcular a idade usando o ano atual menos o ano de nascimento
    Caso a pessoa tenha essa idade (calc) menor que 21 anos, irá cair no if, assim acrescentando mais 1 para o pessMenor e mostrando sua idade
    Caso for False para else, a pessoa tem 21 anos ou mais, assim irá acrescentar mais 1 para o pessMaior e mostrará a idade
'''
