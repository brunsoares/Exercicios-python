import PySimpleGUI as gui #Importando biblioteca externa, e armazenando como gui

test = [[gui.Text("Hello World!!!")],
        [gui.Text("=*"*20)],
        [gui.Text("É muito dahora isso ;-;")],
        [gui.Button('Pressione aqui')]]    #Criando conteúdo do programa, para o texto Text() e botão Button()

wind = gui.Window('Primeiro code na GUI', test)     #Criando a janela, função Window() recebe o nome da janela, e o conteúdo
wind.read()     #Depois ela precisa ser lida, usando o read() para ler o conteúdo do código
wind.close()    #Por fim close() para fechar o programa depois de rodar todo o código

'''
    Documentação = 
    https://pypi.org/project/PySimpleGUI/
    https://pysimplegui.readthedocs.io/en/latest/
'''
