#pegando número
nm = int(input('Digite um número: '))
c = nm
f = 1 #pois começa a multiplicação por 1, multiplicação limpa
print('Calculando o fatorial de {}! = '.format(nm), end="")
while c > 0:
    print('{} '.format(c), end="")
    #Apenas para deixar bonito
    if c > 1:
        print('x ', end="")
    else:
        print('= ', end="")

    #Calculo da fatorial
    f *= c
    c -= 1
print('{}'.format(f))

'''
    Programa para calculo de fatorial
    Primeiro pegamos o valor do usuário armazenado em nm
    Assim criamos c que receberá nm e f que receberá 1
    Depois é mostrado um print de decoração
    E entra no loop, enquanto o c for maior que 0
    Depois nas verificações o if entra caso o c for maior que 1
    Onde irá printar a formatação (deixando bonito, ou quase isso)
    O calculo se baseia em f receber a multiplicação de c
    E cada loop c irá diminuir 1, até chegar em 0 e cancelar o loop
    Depois é printado o resultado formatado
'''
