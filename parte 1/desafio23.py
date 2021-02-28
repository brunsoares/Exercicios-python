#pegando um numero
num = int(input('Digite um numero com 4 digitos: '))

#Separando
n1 = num // 1000 % 10 #casa do milhar
n2 = num // 100 % 10 #casa da centena
n3 = num // 10 % 10 #casa da dezena
n4 = num // 1 % 10 #casa da unidade

#Mostrando
print('Seu número é {}\n'
      'Tem {} milhar\n'
      'Tem {} centena\n'
      'Tem {} dezena\n'
      'Tem {} unidade'.format(num, n1, n2, n3, n4))

'''   
      Para esse exercicio o usuário vai digitar um valor inteiro e será armazenado em num
      Para fazer a separação do número foi usado 4 variaveis, um para cada digito
      Cada variavel baseia seu calculo em pegar o num e fazer a divisão inteira por 1000, 100, 10 ou 1
      E depois Dividir e ver o resto da divisão (modulo) por 10, assim deixando cada valor separado em uma variavel
      O print mostra cada valor separado pelas variaveis n1, n2, n3, n4
'''
