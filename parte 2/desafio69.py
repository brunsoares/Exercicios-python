from time import sleep
cIda = 0
cMas = 0
cFem = 0
while True:
    print('-='*5, 'Novo cadastro', '=-'*5)
    ida = int(input('Digite sua idade: '))

    sex = str(input('Digite seu sexo: [M/F] ')).strip().upper()
    while sex != 'M' and sex != 'F':
        print('\033[31mInsira um sexo válido\033[m')
        sex = str(input('Digite seu sexo correto: [M/F] ')).strip().upper()

    dec = str(input('\nVocê quer fazer outro cadastro? [S/N] ')).strip().upper()
    while dec != 'S' and dec != 'N':
        print('\033[31mQual a sua decisão? insira novamente\033[m')
        dec = str(input('Você quer fazer outro cadastro? [S/N] ')).strip().upper()

    #Verificações
    # maior de 18
    if ida > 18:
        cIda += 1

    # quant homens
    if sex == 'M':
        cMas += 1

    #quant mulher < 20
    if sex == 'F' and ida < 20:
        cFem += 1

    #parar programa
    if dec == 'N':
        print('Cancelando processo de cadastros...')
        print('\033[31mADEUS')
        sleep(2)
        break

print('-='*5, 'Informações geradas', '=-'*5)
print('\033[m{} pessoas tem mais que 18 anos\n'
      '{} homens foram cadastrados\n'
      '{} mulheres com menos de 20 anos'.format(cIda, cMas, cFem))

'''
    Analisando dados até o usuário querer parar
    Primeiro importamos o sleep de time, apenas para melhorar o programa (opcional)
    Depois criamos 3 variaveis de controle zeradas, cIda, cMas, cFem
    Dentro do while True, O usuário vai interagir colocando a idade e o sexo, armazenados em ida e sex
    Depois temos dois loops para checar, o primeiro enquanto o sex não for 'M' ou 'F', o programa irá pedir novamente o sexo da pessoas
    Por fim o usuário interage colocando na dec se deseja continuar ou não [S/N]
    A segunda verificação com o loop, é para checar se o valor está dentro de 'S' ou 'N', caso não esteja vai pedir novamente
    Agora a parte de verificações, onde a primeira se baseia em quantas pessoas tem mais de 18 anos
    Caso seja True, a variavel cIda acrescenta 1
    A próxima é sobre quantos homens foram cadastrados, assim se o sex for igual a 'M', cMas irá incrementar 1
    Por fim se o sex for igual a 'F' e a idade for menor que 20 anos, chegamos na última verificação onde cFem irá incrementar mais 1
    A última checagem é sobre a decisão do usuário onde caso ele tenha decidido parar (N) irá fechar o loop e terminar o programa
    Por fim o print mostrará os resultados aos usuários com base nas verificações
'''
