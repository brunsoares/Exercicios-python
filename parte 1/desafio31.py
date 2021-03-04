#pegando a distancia da viagem
viagemKm = int(input('Digite a distância em km do seu destino: '))

if viagemKm <= 200:
    valPass = viagemKm * 0.50
    print('A viagem selecionada deu {}km e o preço da passagem é R${:.2f}'.format(viagemKm, valPass))
else:
    valPass = viagemKm * 0.45
    print('A viagem selecionada deu {}km ultrapassando o limite de viagens casuais\n'
          'O preço ficou em R${:.2f}'.format(viagemKm, valPass))

'''
    O programa tem como objetivo calcular o valor da passagem
    Primeiro ele pede um valor inteiro que será armazenado em viagemKm
    Logo depois a verificação para achar o primeiro preço
    Se a viagemKm for MENOR ou IGUAL a 200, entrou na condição True, assim vai usar os comandos a seguir
    A variavel valPass pega o valor da viagemKm e multiplica por 0.5, preço da passagem para 200 ou menos KM
    Depois é printado o total de km seguido prelo preço
    Caso a condição der False, ou seja, não entrar no if, cai para o else
    No else o valPass faz o mesmo calculo com viagemKm, porém o preço muda, agora sendo 0.45
    Logo depois é printado novamente os resultados
'''
