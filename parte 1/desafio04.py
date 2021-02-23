val = input('Digite algo para ver as informações: ')
print('O tipo do valor digitado é {}'.format(type(val)))

#Mostrando todas as opções
num = val.isnumeric()
alp = val.isalpha()
alpNum = val.isalnum()
low = val.islower()
up = val.isupper()
asc = val.isascii()
dec = val.isdecimal()
dig = val.isdigit()
idn = val.isidentifier()
ptn = val.isprintable()
spc = val.isspace()
tlt = val.istitle()

print('O valor digitado é um número? {}'.format(num))
print('O valor digitado é uma letra? {}'.format(alp))
print('O valor digitado é tanto um número quanto uma letra? {}'.format(alpNum))
print('O valor digitado está em minusculo? {}'.format(low))
print('O valor digitado está em maiusculo? {}'.format(up))
print('O valor digitado encontra-se na tabela ASCII? {}'.format(asc))
print('O valor digitado é um decimal? {}'.format(dec))
print('O valor digitado são todos digitos? {}'.format(dig))
print('O valor digitado é um identificador? {}'.format(idn))
print('O valor digitado é printavel? {}'.format(ptn))
print('O valor digitado é um espaço? {}'.format(spc))
print('O valor digitado está capitalizada? {}'.format(tlt))

"""
Funcionamento do código

A variavel val recebe um valor, sendo string seu tipo;
Depois usamos diversas funções próprias para verificar caracteristicas do val;
E depois é printado na tela cada função, com o .format()
"""
