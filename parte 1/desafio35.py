#Pegando os valores da reta
rt1 = float(input('Digite o valor da reta 1: '))
rt2 = float(input('Digite o valor da reta 2: '))
rt3 = float(input('Digite o valor da reta 3: '))

checkRt1 = rt1 < (rt2 + rt3) #a reta tem q ser menor que a soma das outras
checkRt2 = rt2 < (rt1 + rt3)
checkRt3 = rt3 < (rt1 + rt2)

if checkRt1 == True and checkRt2 == True and checkRt3 == True:
    print('Dada as informações é possivel fazer um triângulo')
else:
    print('Não é possivel formar um triângulo, troque as informações')

'''
    Programa para checar se pode formar um trinângulo com valores do usuário
    Primeiro pegamos 3 valores para as 3 retas, armazenado em rt1, rt2, rt3
    Depois usamos o checkRt1, checkRt2, checkRt3 para checar se as linhas podem ser usadas no triângulo
    OBS: A linha tem que ser menor que a soma das outras
    Assim na verificação apenas colocamos se cada checkRt deu True
    Caso cada um tenha dado True, OBRIGÁTORIAMENTE todos precisam dar True
    É printado que é possivel montar um trinângulo
    Caso for False qualquer condição
    É printado que não é possivel montar um trinângulo
'''
