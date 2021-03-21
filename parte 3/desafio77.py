#criando tupla aleatoria
tupla = ('Batata', 'Pizza', 'Videogame', 'Celular', 'Musica',
         'Sorvete', 'Python', 'Sono', 'Dormir', 'Jogar')

print('Contagem de vogal')

for i in tupla:
    print(f'\nNa palavra \033[35m{i}\033[m temos = ', end="")
    for lt in i:
        #Se lt estiver dentro de 'a e i o u' vai ser igual a true
        if lt in 'a e i o u':
            print(f'\033[32m{lt}\033[m', end=" ")

'''
    Esse programa irá contar as vogais de uma série de valores da tupla
    Primeiro criamos uma tupla com alguns valores, armazenados em tupla
    Depois temos entra no loop, o i irá rodar a tupla
    Dentro do loop tem um print para mostrar a palavra e outro loop com lt dentro do i
    Ou seja, tem um loop para o i rodar sobre a tupla, e outro para lt rodar sobre i
    Caso lt esteja dentro (in) de a e i o u (vogais) vai printar lt, sendo essas as vogais
'''
