def ficha(nome="Fulano", gols='0'):
    if nome == "":
        nome = 'Fulano'
    if gols == "":
        gols = 0
    return f'O jogador {nome}, marcou {gols} gols no torneio'

jog = str(input('Digite o nome do jogador: ')).strip().title()
gol = str(input('Digite a quantidade de gols no torneio: '))

resp = ficha(jog, gol)
print(resp)

'''
    Programa que irá mostrar o resultado, mesmo com ausência de dados
    Primeiro criamos a função ficha() com dois parametros, opcionais
    Dentro da função, caso o nome seja vazio, o nome recebe valor 'Fulano'
    E caso gols seja vazio, gols recebe 0
    Por fim retorna o valor do nome e gols
    Fora da função, o usuário interage duas vezes com o nome do jogados e gols
    OBS: o gols foi tratado como string, para verificar se estava vazio sem aparecer erros
    Em seguida resp recebe a inicialização de ficha() com parametros do usuário
    Por fim é printado o resp
'''
