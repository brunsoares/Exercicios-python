import PySimpleGUI as gui

layout = [[gui.Text("Digite seu nome por favor")],
          [gui.Input(size=(70, 1), key='Name')],        #Definindo valores de tamanho para caber a informação
          [gui.Text(size=(70, 1), key='ListName')],     #Definindo Key para usar como indicador para interações
          [gui.Button('Mágica'), gui.Button('Tchau ;-;')]]

window = gui.Window("Programa de Boas vindas", layout)

#Loop para interagir com o user sem fechar o programa
while True:
    #Values são os valores armazenados em inputs por exemplo, que o usuario interage
    event, values = window.read()   #Events se tratam dos eventos dentro do programa, como clicar e interagir
    #Caso o usuario queira sair do programa
    if event == gui.WINDOW_CLOSED or event == 'Tchau ;-;':
        break #Programa fecha

    #Mostrando interação com o usuario | Escrevendo na tela do programa
    window['ListName'].update(f'Hello World {str(values["Name"]).title()}, Seja Bem vindo ao programa', text_color='purple')

window.close()

'''
    Programa parecido com o anterior porém ele utiliza de loop para que o programa interaja até o usuário decidir fechar o mesmo
    Programa interage na interface mesmo, mostrando a mensagem ao usuário na hora
'''
