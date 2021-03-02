#pegando a frase
frase = str(input('Digite uma frase qualquer: ')).strip()
fraseCorr = frase.lower()
#contagem de a
allA = fraseCorr.count('a')
firstA = fraseCorr.find('a')
lastA = fraseCorr.rfind('a') #rfind começa a procura do lado direito right

print('Sua frase contém {} "a" '.format(allA))
print('O primeiro "a" aparece no indice {} ou na letra {}'.format(firstA, firstA + 1))
print('O último "a" aparece no indice {} ou na letra {}'.format(lastA, lastA + 1))

'''
    O programa começa pedindo uma frase do usuário, que será armazenada em frase, dentro dessa variavel tem uma função strip()
    O strip() serve para retirar espaços antes e depois do valor, caso o usuário aperte diversas vezes espaço
    A variavel fraseCorr deixa tuda a variavel em caixa baixa
    Depois vem a checagem, primeiro quantas letras 'a' tem na frase
    A variavel allA usa o fraseCorr junto com a função count() para contar quantos 'a' tem
    O firstA pega o valor de fraseCorr e usa junto o find() para achar o primeiro 'a' digitado (da esquerda -> para direita)
    O lastA pega o valor de fraseCorr e faz o contrario, usa o rfind() para achar o 'último' 'a', que no caso seria o primeiro da direita -> para esquerda
    Depois os valores são printados com o print, OBS: o firstA/lastA estão com +1 pois o indice começa a contar do 0, ou seja iria sempre ficar um valor antes do que costumamos ler
'''
