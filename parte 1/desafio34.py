#pegando salario funcionario
salFun = float(input('Digite seu salário: '))

if salFun > 1250:
    calcAum = salFun * 0.10
    aum = salFun + calcAum
    print('O seu novo salário teve um aumento de 10% e ficou R${:.2f}'.format(aum))
else:
    calcAum = salFun * 0.15
    aum = salFun + calcAum
    print('O seu novo salário teve um aumento de 15% e ficou R${:.2f}'.format(aum))

'''
    Programa para aumento de % de salário dependendo da quantidade de salário
    Primeiro pegamos o valor do salário, armazenado em salFun
    Na verificação, Se salFUn for maior que 1250, será True para if
    Assim o calcAum vai calcular 10% do salário do funcionário
    E a variavel aum vai incrementar o calcAum no salário
    Depois printará o resultado do novo salário
    Caso a condição seja False, entra no else
    Assim o calcAum vai fazer a mesma função porém agora com 15%
    O aum vai incrementar esses 15% no salário
    E o resultado do novo salário será printado
'''
