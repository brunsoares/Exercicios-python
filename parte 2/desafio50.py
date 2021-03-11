#Colocando acumulador para somar
somaPar = 0

for n in range(0, 6):
    num = int(input('Digite algum número: '))
    #vendo se o num eh par
    if num % 2 == 0:
        somaPar += num
print('A soma dos números pares digitados por você é igual a {}'.format(somaPar))

'''
    Primeiro criamos uma variavel para ser acrescentada, a somaPar com valor inicial de 0
    No loop o n irá percorrer o limite de 0 até 5
    Dentro do loop, vai tem uma interação com usuário, onde digitará um valor inteiro armazenado em num
    OBS: A interação irá acontecer sempre que voltar o loop
    Dentro do loop tem uma verificação se o valor digitado do usuário for par, caso True a variavel somaPar vai acrescentar de num
    Por fim saindo do loop, mostrará pelo print() a soma de todos os 6 valores digitados
'''
