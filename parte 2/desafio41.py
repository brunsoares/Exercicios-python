import datetime

#pegando ano de nascimento
anoUsu = int(input('Digite o seu ano de nascimento: '))

#ano atual
anoAtu = datetime.date.today().year

#calculo
calc = anoAtu - anoUsu

#validação das categorias
if calc <= 9:
    print('Você está na categoria: \033[1;32mMIRIM')
elif calc > 9 and calc <= 14:
    print('Você está na categoria: \033[1;36mINFANTIL')
elif calc > 14 and calc <= 19:
    print('Você está na categoria: \033[1;31mJUNIOR')
elif calc > 19 and calc <= 25:
    print('Você está na categoria: \033[1;34mSÊNIOR')
else:
    print('Você está na categoria: \033[1;35mMASTER')

'''
    Nesse programa será visto em qual categoria a pessoa está para o esporte
    Primeiro importamos a biblioteca datetime para pegar o ano atual
    O usuário vai informar o ano de nascimento armazenado em anoUsu
    A variavel anoAtu vai pegar usando o date.today().year o ano atual
    A variavel calc vai pegar o valor do ano atual menos o nascimento para ter a idade
    Na verificação se baseia na idade, ou seja, o primeiro if será True se o calc (idade) for menor ou igual a 9 anos
    Em seguida temos outra entre acima de 9 e menor igual a 14 anos
    Outra com acima de 14 anos e menor igual a 19 anos
    A última acima de 19 e menor ou igual a 25
    Caso nenhuma bata True, caira no else acima de 25 anos
    Em todas o print está mostrando a categoria definida para a pessoa, usando cores e parametros para deixar a letra em negrito
    \033[x;y;zPalavra\033[m
    Nesse exemplo o x é o estilo da palavra, negrito ou sublinhado exemplo
    O y é a cor das letras, e o z a cor de fundo da palavra
'''
