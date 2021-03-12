#pegando valor
num = int(input('Digite um valor: '))
contVZ = 0

for i in range(1, num + 1):
    if num % i == 0:
        #significa que ele não eh primo pois foi dividido por mais de 2
        contVZ += 1

if contVZ == 2:
    #ele é primo
    print('O {} é primo pois so foi dividido {} vezes'.format(num, contVZ))
else:
    print('O {} não é primo pois foi dividido {} vezes'.format(num, contVZ))

'''
    Primeiro pegamos o valor para ser armazenado em num
    Criamos também uma variavel contVZ com valor 0 para ser acrescentada posteriormente
    Dentro do loop o i vai rodar sobre o limite de 1 até o número + 1 (para pegar o valor do número por inteiro)
    Assim cada loop vai entrar no if, sendo este se o num for divisivel por i e restar 0, assim não sendo primo
    Onde so vai acrescentar o contVZ para mais 1
    Caso o contVZ for igual a 2 vai cair em um if (Fora do loop)
    Onde caso for True, ele será primo, assim mostrando quantas vezes foi dividido usando a variavel contVZ
    Caso for False, ele cairá no else, mostrando que não é primo e foi dividido mais de 2 vezes
    OBS: número primo só é divisivel por ele mesmo e por 1
'''
