maior = 0
menor = 0

#pegando pesos
for p in range(0, 5):
    peso = float(input('Digite o seu peso: '))

#Se for a primeira pessoa, o peso maior e menor vao ser o mesmo pois não tem outro dado a comparar
    if p == 1:
        maior = peso
        menor = peso
#Caso não for a primeira pessoa, tem dados para fazer a comparaçao
    else:
        if peso > maior: #Se for maior que o peso atual, esse peso vira o novo atual
            maior = peso
        if peso < menor: #Se for menor que o peso atual, esse peso vira o novo atual
            menor = peso
print('O maior peso visto foi de {}Kg'.format(maior))
print('O menor peso visto foi de {}Kg'.format(menor))

'''
    Nesse programa irá analisar o maior e menor peso entre 5 pessoas
    Primeiro criamos duas variaveis de controle, com valor 0, maior e menor
    Logo em seguida entra no loop onde p irá rodar 5 vezes
    A variavel peso irá armazenar o peso em float do usuário
    No if caso o p for igual a 1, ou seja primeira pessoa cadastrada, o maior e menor receberá o peso dessa pessoa, pois não tem outro a comparar ainda
    Caso não for a primeira pessoa vai cair no else, dentro do else temos dois if's
    Caso o peso (atual da pessoa que não é a pessoa 1) for maior que o maior (peso da primeira pessoa), o maior receberá esse peso
    Caso o peso (atual da pessoa que não é a pessoa 1) for menor que o menor (peso da primeira pessoa), o menor receberá esse peso 
    No final mostrará o maior e menor peso das pessoas pelos prints()
'''
