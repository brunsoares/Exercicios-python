#pegando valores da progressão aritmetica
firstTermo = int(input('Digite o primeiro termo: '))#numero q começa a progressão
razao = int(input('Digite a razão: '))#contagem da progressão
limit = firstTermo + (10 - 1) * razao #Formula para contagem do limite do termo, 10 é o tanto que vai ser o limite

for i in range(firstTermo, limit + 1, razao):
    print('{}'.format(i), end=' -> ')
print('ACABOU A P.A.')

'''
    O programa consiste em mostrar uma P.A, Progressão aritmética
    Primeiro pegamos o termo da P.A, que o usuário vai digitar e armazenar em firstTermo
    Em seguida ele digita a razao, armazenado na variavel razao
    A variavel limit usa uma formula para achar o limite da P.A
    Em seguida entra no loop, onde a variavel i roda sobre o limite que começa no firstTermo até o limit + 1, seguindo a contagem da razao
    Para cada loop vai printar o i que é o valor da P.A, quando acabar mostrará o print finalizando o programa
'''
