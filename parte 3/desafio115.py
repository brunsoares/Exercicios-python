import desafio115mod
from time import sleep

#manipulando arquivo
arq = 'arquivoteste115.txt'

if not desafio115mod.arquivoExiste(arq):#se o aquivo for false
    desafio115mod.criarArquivo(arq)

while True:
    resposta = desafio115mod.menu(['Listar cadastrados', 'Cadastrar cliente', 'Sair do programa'])
    if resposta == 1:
        desafio115mod.lerArquivo(arq)
    elif resposta == 2:
        desafio115mod.cabeca('Novo cadastro')
        nome = str(input('Digite o nome: ')).strip().title()
        idade = desafio115mod.leiaint('Digite a idade: ')
        desafio115mod.cadastrar(arq, nome, idade)
    elif resposta == 3:
        desafio115mod.cabeca('Saindo do programa')
        break
    else:
        print('\033[31mOpção INVALIDA\033[m')
    sleep(2)

'''
    Esse programa criará e armazenará dados de pessoas, mesmo depois se for fechado
    Primeiro importamos o desafio115mod.py, módulo criado e a função sleep() de time
    Primeiro vamos manipular o arquivo, assim a variavel arq recebe o nome do arquivo
    Caso não exista esse arquivo na função arquivoExiste(), ele criará um pela função criarArquivo()
    No loop infinito, a variavel resposta chama a função menu() que armazena um dicionário de opções
    Agora para ler as opções caso a resposta for igual a 1, é chamado a função lerArquivo() que mostrará o arquivo
    Caso for 2, entra em novo cadastro, onde o usuário informa nome e idade, e depois pela função cadastrar() cadastra a nova pessoa
    Por fim se a resposta for 3, fechará o programa
    Também tem a caso não for nenhuma opção, onde gerará o print() opção invalida
    No fim do loop colocamos um sleep() de 2 segundos para melhorar a interação
'''
