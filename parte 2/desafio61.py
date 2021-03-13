#lendo os numeros
termo = int(input('Digite o termo da PA: '))
razao = int(input('Digite a razao da PA: '))
limit = termo + (10 - 1) * razao #10 eh a quant de valores mostrados

while termo <= limit:
    print(termo, end=' -> ')
    termo += razao
print('Acabou a P.A')

'''
    Esse programa é uma adaptação do programa 51 da parte dois, porém agora usando while
    Primeiro pegamos informações do usuário como o termo e a razao
    A variavel limit usa a mesma formula do exercício 51 para achar o limite da P.A
    No while, enquanto o termo for menor ou igual a limit, irá continuar o loop
    Cada loop é printado o termo, e em seguida o termo acrescenta a razao
    Por fim é mostrado um print encerrando o programa
'''
