expr = str(input('Digite sua expressão: '))
pilha = [] #onde vai ficar os ()
for simbol in expr:
    if simbol == '(':
        #simbolo igual a ( adicionar a lista
        pilha.append('(')
    elif simbol == ')':
        if len(pilha) > 0:
            pilha.pop() #se o tamanho da pilha estiver acima de 0, exclui o conjunto de ()
        else:
            #simbolo igual a ) adicionar a lista
            pilha.append(')')
            break

#Se sobrar 0 quer dizer que não a pendencia de () expressão valida
if len(pilha) == 0:
    print('Sua expressão está \033[32mcorreta\033[m')
else:
    #Pilha tem alguma pendencia de ()
    print('Sua expressão está \033[31mincorreta\033[m')

'''
    Esse programa irá analizar uma expressão matématica e dizer se o formato está correto
    Primeiro o usuário vai interagir colocando a expressão armazenado em expr
    Criamos também uma lista vazia chamada pilha
    Dentro do loop for, simbol irá rodar sobre expr, caso simbol for igual a (, adiciona na pilha o (
    Mesmo caso para se simbol for ), porém se o tamanho da pilha for maior que 0, vai excluir o conjunto () pelo pop()
    Caso o tamanho não for maior que 0, é adicionado o ) pelo append()
    Na verificação de valido ou invalido, caso o tamanho da pilha for igual a 0, significa que todos os parenteses foram fechados e excluidos pelo pop()
    Ou seja a expressão está sem pendência de () e está correta
    Caso contrário, a espressão tem pendência e está incorreta
'''
