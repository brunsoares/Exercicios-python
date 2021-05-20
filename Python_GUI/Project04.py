import PySimpleGUI as gui

#Layout primeiro programa em que pegara os valores
layout = [[gui.Text("Digite valores para criar sua matriz.")],
          [gui.Input(size=(10, 1), key='val1'), gui.Text("Valor para Coluna")],
          [gui.Input(size=(10, 1), key='val2'), gui.Text("Valor para Linha")],
          [gui.Text(size=(25, 1), key='alert')],
          [gui.Button("Montar seu programa de matriz", key='Montar'), gui.Button("Sair ;-;")]]

window = gui.Window("Programa de montar matriz", layout)

#Loop para interagir
while True:
    events, values = window.read()
    #Para fechar o programa
    if events == gui.WINDOW_CLOSED or events == 'Sair ;-;':
        break

    #Continuação do loop, montagem de outro programa com as matrizes
    val1 = values['val1']
    val2 = values['val2']
    #checando para saber se o valor é numerico ou não
    if not val1.isnumeric() or not val2.isnumeric():
        window['alert'].update('Valores incorreto!, favor checar', text_color='red')
        #print("Erro valor invalido")
    else:
        window['alert'].update('Valores válidos!, obrigado', text_color='green')
        num1 = int(val1)
        num2 = int(val2)
        #print(num1, num2)

        #Montando novo programa com os valores para as matrizes
        #for usado para delimitar o limite das matrizes pelos valores do usuario
        layout2 = [[gui.Button(f'{lin}, {col}') for lin in range(num1)] for col in range(num2)]
        #criando janela
        window2 = gui.Window("Matriz personalizada", layout2)
        window2.read(close=True)

window.close()

'''
    Programa que pede valores ao usuário para criar outra janela, sem fechar a anterior, com matrizes
    Com base no valor em que o usuário desccreveu anteriormente, com sistema impossibilitando a digitação
    De outro valor sem ser númerico, assim validando corretamente antes de ser gerado.
'''
