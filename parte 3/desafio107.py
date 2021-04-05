#import desafio107mod
from modulosUtil import moeda

num = int(input('Digite um valor: '))
print(f'O aumento de 10% deu: R$ ', end="")
#print(desafio107mod.aumentar(num, 10))
print(moeda.aumentar(num, 10))
print(f'O desconto de 10% deu: R$ ', end="")
#print(desafio107mod.diminuir(num, 10))
print(moeda.diminuir(num, 10))
print(f'A metade desse valor é: R$ ', end="")
#print(desafio107mod.metade(num))
print(moeda.metade(num))
print(f'O dobro desse valor é: R$ ', end="")
#print(desafio107mod.dobrar(num))
print(moeda.dobrar(num))

'''
    Esse programa mostrará informações sobre valores com funções e módulos
    Primeiro programa usando modulos, modulos seria um arquivo extra onde é colocado todas as funções para deixar o programa mais limpo
    Assim esse programa acompanha o desafio107mod.py, e posteriormente o modulosUtil
    A explicação desse exercicio será com base no modulosUtil, caso queira ver usando o desafio107mod.py, apenas tirar os comentários
    A modulosUtil é uma pasta criada que dentro contém outras duas pastas, dados e moedas, cada uma tem sua explicação
    O formato é como se fosse uma biblioteca, estilo random ou time, porém própria nossa
    Primeiro importamos moeda, que está em modulosUtil, que contém as funções usadas
    Dentro desse programa apenas pedimos a interação do usuário armazenado em num
    Em seguida printamos os resultados e chamamos as funções de moeda, passando num como parametro
    Para entender as funções acesse o desafio107mod.py ou a pasta modulosUtil e suas pastas
'''
