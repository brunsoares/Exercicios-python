#Pegando o nome completo
nome = input('Digite seu nome completo: ')

#transformando
nomeUp = nome.upper()
nomeLow = nome.lower()

#Nome sem espaços
#Dividindo
divNome = nome.split()
#print(divNome)

#Pegando primeiro nome
firstNome = divNome[0]
tamFirstNome = len(firstNome)
#print(firstNome)

#Juntando
nomeJunt = ''.join(divNome)
#print(nomeJunt)
tamNomeJunt = len(nomeJunt)

#mostrando
print('Seu nome em maiusculo é {}'.format(nomeUp))
print('Seu nome em minusculo é {}'.format(nomeLow))
print('Seu nome *sem espaços* tem {} de tamanho'.format(tamNomeJunt))
print('Seu primeiro nome {} tem exato {} de tamanho'.format(firstNome, tamFirstNome))

'''
    Nesses programas (22 - 27) é focado no tratamento de strings
    Primeiro a variavel nome recebe uma string do usuário
    Em seguida temos a variavel nomeUp que usa a função upper()  para deixar tudo em caixa Alta
    Depois nomeLow que usa a função lower() para fazer o contrário
    Para fazer o resto das verificações, usamos a divNome que usa o split() que separa os nomes pelo espaço deixando-os em uma lista
    Para pegar o primeiro nome usa a função firstNome que usa o indice [0] que é usado nas listas para achar o primeiro valor
    Em seguida a variavel tamFirstNome uma a função len() que pega o tamanho da string
    Para juntar os nomes usamos a variavel nomeJunt que usa a função join() que vai juntar a lista os separando apenas pelo '' (ou seja sem espaços)
    E a variavel tamNomeJunt usa o len() para saber o valor do nome completo sem espaços
    Por fim cada verificação é printada no print e mostrada ao usuário
'''
