def leiaint(n):
    while True:
        try:
            n = int(input('Digite um valor int: '))
        except Exception as error:
            print('Número invalido, tente novamente...')
            print(f'Invalido pois deu esse erro: {error.__class__}')
            continue #o loop
        else:
            return n


def linha(tam=42):
    return '-'*42


def cabeca(txt):
    print(linha())
    print(txt.center(42))#centralizando a 42 espaços
    print(linha())


def menu(lst):
    cabeca('Menu principal')
    c = 1
    for itens in lst:
        print(f'{c} -> {itens}')
        c += 1
    print(linha())
    opc = leiaint('Sua opção: ')
    return opc

#----------------------------------Acabou parte de menu------------------------
#----------------------------------Começa parte de manipular arquivo-----------
def arquivoExiste(nome):
    try:
        a = open(nome, 'rt') #rt é para abrir e ler  ReadText
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(nome):
    try:
        a = open(nome, 'wt+') #wt é para escrever WriteText, o + é caso ele não exista crie
        a.close()
    except:
        print('Erro na criação do arquivo')
    else:
        print(f'Arquivo {nome} criado com sucesso')

#lendo arquivo
def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Falha na hora de abrir o arquivo')
    else:
        cabeca('Lista de pessoas')
        for i in a:
            dado = i.split(';')#separando os dados
            dado[1] = dado[1].replace('\n', '')#tirando os espaços
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()

#cadastro de pessoas
def cadastrar(arq, nome='Desconhecido', idade=0):
    try:
        a = open(arq, 'at')#a de append colocar coisas no texto o t é de texto
    except:
        print('Houve erro no cadastro ')
    else:
        try:
            a.write(f'\n{nome};{idade}')
        except:
            print('Houve um erro na digitação do arquivo')
        else:
            print(f'Novo registro de {nome} com sucesso')
            a.close()

'''
    Esse módulo baseia no funcionamento do desafio115 apenas
    Primeiro criamos a função leiaint(), a mesma explicada no exercício 104, porém aprimorada para tratar erros
    Na função linha() apenas retorna uma linha de 42 de tamanho, juntamente com a função cabeca() que mostra linha() e um texto centralizad, essas apenas de decoração
    Na função menu(), listamos cabeca() como menu principal, e damos valor inicial a c de 1
    Com isso entramos no loop for onde itens vão rodar pelo parametro, e em cada loop mostra c e itens
    Por fim c incrementa 1, para continuar a lógica do loop, e o programa pede interação com o usuário e retorna a mesma
    Até o momento foi apenas para menu essas funções, agora a manipulação de arquivos
    A arquivoExiste(), primeiro tentará abrir, com a função open() e fechar um arquivo com esse nome, caso não consiga ele emitirá o erro de arquivo não encontrado, retornando false
    Caso consiga, ele retorna apenas True, sendo que o arquivo existe
    No caso de criarArquivo(), ocorre caso a anterior for false, assim, ele usará o open() porém mudando o segundo parametro para assim escrever no arquivo
    Caso não consiga escrever, ele emitirá um print() e caso consiga, ele printará que o arquivo foi criado
    Para ler o arquivo foi usado a função lerArquivo(), que primeiramente tenta abrir o arquivo, caso não consiga emitirá um erro
    Caso consiga ele troca a cabeca() por lista de pessoas, e com o for entrará no arquivo e mostrará os dados formatados com o fatiamento de strings
    Por fim, finally, o arquivo é fechado pelo close()
    No cadastrar() ele recebe dois parametros opcionais pré definidos, assim ele tentará abrir o aquivo, caso tenha falha ele irá informar
    Caso consiga, o arquivo tenta usar a função write() para escrever os dados, caso não consiga ele retorna novamente
    Porém caso consiga ele completa o cadastro e informa o usuário
    OBS: essas funções estão ligadas ao exercício 115
'''
