#pegando numero usuario
nm1 = int(input('Digite um valor: '))
nm2 = int(input('Digite outro valor: '))
nm3 = int(input('Digite mais um valor: '))
nm4 = int(input('Digite o último valor: '))

#armazenando na tupla
tupla = (nm1, nm2, nm3, nm4)
#print(tupla)

#Checagem conforme o exercicio
ctn9 = 0
ctnPar = 0

for pos, num in enumerate(tupla):
    #Checagem quantos 9's tem
    if num == 9:
        ctn9 += 1

#resultados
print(f'Os números listados foram: {tupla}')

if ctn9 > 0:
    print(f"Entre os números digitados, tem {ctn9} 9's no programa")
else:
    print(f"Não foi digitado nenhum 9")

#numero 3 na primeira posição
if nm1 == 3 or nm2 == 3 or nm3 == 3 or nm4 == 3:
    num3 = tupla.index(3) + 1
    print(f'O primeiro 3 aparece na posição {num3}')
else:
    print('O número 3 não aparece nenhuma vez')

print('Esses foram os números pares no programa: ', end="")
for i in tupla:
    # Checagem numero par
    if i % 2 == 0:
        ctnPar += 1
        print(i, end=" ")
print(f'\nTem {ctnPar} números pares no programa')

'''
    Esse programa verifica diversas condições de uma tupla do usuário
    Primeiro o usuário interage com 4 valores armazenados de nm1 a nm4
    Em seguida a variavel tupla cria uma tupla com esses valores
    Depois é criado duas variaveis de controle zeradas, cnt9 e ctnPar
    No loop for usamos duas variaveis pos e num para o enumerate() na tupla
    Assim na verificação dentro do loop, se o num for igual a 9 o ctn9 incrementa 1
    Depois é mostrado um print iniciando os resultados
    No if em seguida temos caso cnt9 for maior que zero, onde mostrará a quantidade de 9's na tupla
    Caso não bata e caia no else, apenas é mostrado que não tem nenhum 9
    No outro if irá verificar se tem um 3 na tupla
    Caso então as variaveis nm1, nm2, nm3, nm4 tenha valor 3 alguma, entra no if
    Assim dentro do if num3 pega o index() de 3 + 1 (+1 é apenas para deixar em uma visualização normal ao usuário que não está acostumado com contagem começando do 0)
    Depois é printado a posição do 3
    Caso não bata a primeira verificação, mostra que não tem nenhum 3 na tupla
    Por fim temos um print que mostrará os números pares na tupla
    Assim entra no loop onde o i irá rodar sobre a tupla
    E dentro tem a verificação onde se o i for dividido por 2 e restar 0 o número é par
    Onde vai contar o ctnPar incrementando mais 1, e também mostrando para o usuário
'''
