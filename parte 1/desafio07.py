#Pegando as notas do aluno
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
print('A média do aluno foi {:.1f}, se for menor que 7 está reprovado, maior que 7 aprovado'.format(media))

'''
    O usuario vai digitar duas notas (que podem ser float) armazenadas respectivamente em nota1 e nota2
    A variavel média vai calcular primeiro a soma das notas e depois dividir
    OBS: tirar os () irá fazer com que a nota2 seja dividida antes de somar, dando a média errada
    Depois é printado o resultado, usando a formatação "forçada" de deixar uma casa depois da virgula {:.1f}
'''
