#pegando os numeros
soma = 0
for c in range(1, 501):
    #Validando os numeros, primeiro se são impares e depois se sao multiplos de 3
    if c % 2 == 1 and c % 3 == 0:
        soma += c
print('A soma de todos os números impares multiplos de 3 é igual a {}'.format(soma))

'''
    Primeiro criamos uma variavel soma com valor 0, usada depois para acrescentar valor
    Com o loop for criamos c para rodar sobre o limite de 1 até 500
    Dentro do loop tem a verificação para caso se o resto da divisão inteira de c por 2 restar 1 (impar), e se esse valor for divisivel por 3
    Se a condição do if for True, a variavel soma acrescenta valor (+=) sobre c
    Por fim o print mostra o resultado de todos os valores somados que bateram a condição do if
'''
