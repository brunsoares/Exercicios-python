c = 0
s = 0
while True:
    #loop infinito
    n = int(input('Digite um número [Ou 999 para parar]: '))
    if n == 999:
      print('Você decidiu parar o programa')
      break
    c += 1
    s += n
print(f'A soma dos {c} números digitados foi {s}')
#nova forma de representar variavel, fstring

'''
   Outra forma de fazer contagem de valores, porém até o usuário querer parar
   Primeiro criamos duas variaveis de controle zeradas,'c' e 's'
   Depois entra no loop infinito (While True)
   Dentro desse loop o usuário interage colocando um valor em n
   Caso o n for igual a 999, o programa fechará pelo break na verificação
   Caso continue, c acrescenta 1 e s acrescenta o n
   Por fim aparece um print mostrando seus resultados, esse print usa outro formato de fstring 
'''
