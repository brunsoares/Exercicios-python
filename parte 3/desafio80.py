val = []
for i in range(0, 5):
    v = int(input('Digite um valor: '))
    #Checando se é o primeiro ou maior que o ultimo
    if i == 0 or v > val[-1]:#Se for true, adicionar na lista sem problemas
        val.append(v)
    else: #Outros numeros menores
        pos = 0
        while pos < len(val): #Se for menor que o tamanho da lista, continua o loop para verificar
            if v <= val[pos]: #se o numero for menor que o numero na pos adicionar antes
                val.insert(pos, v) #insere o numero (v) na posicao atual (pos)
                break
            pos += 1

print(f'Esses são os valores em ordem crescente = {val}')

'''
    Outro exercício parecido com o anterior, porém ordenando sem usar o sort()
    Primeiro criamos uma variavel val que é uma lista vazia
    No loop o i irá rodar 5 vezes
    Dentro do loop tem a interação com o usuário armazenada em v
    Agora ordenando os valores, caso o i for igual a 0 ou v for maior que val na última posição
    Irá adicionar o valor com o append()
    Caso tenha outros valores menores, cai no else
    Onde é criado uma variavel pos zerada, dentro do while, enquanto pos for menor que o tamanho de val irá ter loop
    Caso o v for menor ou igual a val no indice da pos, irá inserir o valor na posição da pos usando o insert()
    E depois vai dar um break, e incrementar mais 1 para pos
    No fim irá mostrar o print com os valores ordenados
'''
