#pegando nome
nom = str(input('Digite seu nome completo: ')).strip()
#dividindo o nome
divNom1 = nom.split()
#pegando primeiro nome e ultimo
firstNom = divNom1[0]

print('Seu nome é {}'.format(nom))
print('Primeiro nome = {}'.format(firstNom))
print('Último nome = {}'.format(divNom1[len(divNom1)-1])) #pega o tamanho do split e coloca -1 para o ultimo nome

'''
    Primeiro o usuário digita um valor para nom, usando novamente o strip()
    Para dividir o nome usa o divNom1 que pega o nom e usa o split() para formar uma lista
    Para pegar o primeiro nome usa o firstNom que já usa a lista formada pelo divNom1 e pega o valor no indice [0]
    Depois é printado os valores, apenas no último que o indice usado para pegar o último valor foi feito no print
    No caso o divNom1 pega o indice [] no tamanho da lista, isso menos 1, assim ele pegará o valor do último nome
'''
