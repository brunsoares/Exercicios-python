from datetime import date

#função voto
def voto(anoNasc):
    anoAtu = date.today().year
    idad = anoAtu - anoNasc
    #checando idade para condição do voto
    # < 18 não vota >18 obrigatorio, >65 e (>15 e <18) opicional
    if idad > 65 or idad >= 15 and idad < 18:
        return '\033[35mVOTO OPCIONAL\033[m'
    elif idad >= 18 and idad <= 65:
        return '\033[32mVOTO OBRIGATORIO\033[m'
    elif idad < 15:
        return '\033[31mNÃO PODE VOTAR\033[m'



valUsu = int(input('Digite o ano de nascimento: '))
resp = voto(valUsu)
print(f'Sua situação para votar é {resp}')

'''
    Programa para analisar a situação de voto do usuário
    Primeiro importamos a função date da biblioteca datetime
    Assim criamos uma função definida como voto() com um parametro
    Em seguida pegamos o ano atual na variavel anoAtu usando o date.today().year()
    E na variavel idad pegamos a diferença entre o anoAtu e o anoNasc (parametro)
    Caso a idade for menor que 18 e maior igual a 15 ou maior que 65, será dado um return pelo voto opcional
    Caso for maior ou igual a 18 e menor ou igual a 65, será dado um return pelo voto obrigatório
    Por fim caso a idade for menor que 15 o return será que não pode votar
    O return pode se dizer que é o valor retornado de algo, no caso retornado de cada verificação
    Fora da função, pedimos o ano de nascimento do usuário, armazenado em valUsu
    Em seguida criamos a variavel resp que recebe a inicialização da função voto() com parametro valUsu
    Por fim é printado o resp, pelo print()
'''
