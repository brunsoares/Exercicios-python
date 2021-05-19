import PySimpleGUI as gui

layout = [[gui.Text("Informe seu nome:")],
          [gui.Input(key='Name')],
          [gui.Button("Diga Hello")]]

window = gui.Window("Hello World", layout)
events, values = window.read() #Armazenando valores em values

#Lendo os valores para mostrar ao no console
print(f"Hello World {str(values['Name']).title()}, Bem vindo ao programa")

window.close()

'''
    Programa para ler o nome do usuário e mostrar uma mensagem via console juntamente com o nome lançado
'''
