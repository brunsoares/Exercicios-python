def manual(comand):
    return help(comand)

while True:
    cmd = str(input('Digite um comando [fim acaba]: ')).lower().strip()
    if cmd == 'fim':
        print('\033[31mADEUS...\033[m')
        break
    val = manual(cmd)

'''
    Função para retornar o manual de ajuda de um comando
    Primeiro criamos a função manual() com um parametro
    Dentro a função apenas retorna o help() do parametro
    Fora da função temos o loop infinito, onde o usuário vai interagir com a variavel cmd
    Colocando o comando que ele precisa de ajuda, caso ele digite fim, o loop encerra
    Por fim a variavel val chama a função manual para o parametro cmd
'''
