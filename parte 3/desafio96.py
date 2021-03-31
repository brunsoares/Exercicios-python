def area(x, y): #x largura | y comprimento
    s = x * y
    print(f'A área desse terreno é de: {s}m²')


#pegando valores doo usuario
larg = float(input('Digite a largura do terreno em m: '))
comp = float(input('Digite o comprimento do terreno em m: '))
area(larg, comp)

'''
    Primeiro programa usando função, programa que irá calcular a área do local
    Primeiro criamos uma função, usando o def nome_da_função() dentro do () colocar se tiver parametros, nesse caso tem 2
    Dentro da função é o que ela fará quando chamada, assim a variavel s vai armazenar a multiplicação de x e y
    E depois printará o resultado
    Fora da função pedimos dois valores ao usuário, e em seguida chamamos a função usando as variaveis do usuário como parametro
'''
