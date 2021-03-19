#Montando a tupla
numExt = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

#Numero usuario
numUsu = int(input('Digite um Número entre 0 e 20: '))

#Verificando numero invalido
if numUsu > 20 or numUsu < 0:
    print('\033[31mDigite um valor válido ao teste\033[m')

#Pegando a posição e numero no numExt
for pos, num in enumerate(numExt):
    if numUsu == pos:
        print(f'Seu valor é {numUsu} e por extenso é {num}')

print('-*- Acabou -*-')

'''
    Programa para mostrar número por extenso, primeiro programa usando tuplas
    Tupla é um formato de variavel no python, que armazena diversos valores, elas são imutáveis
    Primeiro montamos uma tupla numExt, com valores por extenso de 0 a 20, formato entre ()
    Depois pegamos a interação do usuário,armazenado em numUsu
    Depois tem uma pequena verificação para checar se o valor está fora do limite da tupla, onde caso for True, mostrará número inválido
    Em seguida temos o for que usa duas variaveis, pos e num que irão rodar sobre o enumerate() de numExt
    O enumarate pega o valor de cada indice (armazenado em num) e sua posição (armazenado em pos)
    Caso o numUsu seja igual a pos vai mostrar os valores e assim encerra o loop
    Por fim tem o print encerrando o programa    
'''
