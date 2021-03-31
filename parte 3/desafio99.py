def maior(*num):
    print(f'Esse foi o maior número dos parametros: {max(val)}')


val = []
while True:
    val.append(int(input('Digite um valor: ')))
    dec = str(input('Deseja continuar? [S/N]: ')).strip().upper()
    if dec != 'S':
        print('Você decidiu \033[31mPARAR\033[m')
        break

print(f'Esses foram os valores digitados: {val}\n')
#print(sorted(val))
#print(max(val))
maior(val)

'''
    Programa que irá visualizar o maior valor digitado
    Primeiro criamos uma função maior que receberá apenas um parametro, dentro da função será printado o maior valor do parametro usando o max()
    Fora da função, criamos uma lista chamada val vazia
    No loop infinito, o usuário vai digitar valores que o val irá dar append(), e ele decidirá continuar ou não em dec
    Caso dec for diferente de S loop irá parar pelo break
    Por fim será mostrado os valores digitados em val, e será chamado a função maior() passando val como parametro
'''
