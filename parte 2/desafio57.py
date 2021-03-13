#criando loop
sex = 'm'
while sex != 'F' and sex != 'M':
    sex = str(input('Digite seu sexo [M/F]: ')).upper().strip()
    if sex != 'M' and sex != 'F':
        print('Digite um valor válido: [M/F] ')
    else:
        if sex == 'M':
            print('Seu sexo é Masculino')
        else:
            print('Seu sexo é Feminino')

print('Acabou')

'''
    Programa irá analisar sexo das pessoas usando while
    Primeiro criamos uma variavel de controle sex com valor 'm'
    Em seguida usamos a estrutura while, que significa enquanto tal condição não deixar de ser verdadeira, continua o loop
    Dentro do loop tem a interação do usuário para digitar seu sexo armazenado em sex
    Nas verificações, caso o sexo não seja nem 'M' ou 'F', irá retornar o loop com valor invalido, e pedindo uma nova interação
    Caso seja 'M' ou 'F' cairá no else, onde tem outro if/else
    Onde se o sex for 'M' será masculino, caso contrário (else) será feminino ('F')
    Assim finaliza o loop pois a condição do while foi batida como False, mostrando um print finalizando
'''
