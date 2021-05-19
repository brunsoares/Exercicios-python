import PySimpleGUI as gui #Importando biblioteca externa, e armazenando como gui

#O formato da biblioteca requer o usu de dicionários e listas, por isso foi armazenado em um dicioário
test = [[gui.Text("Hello World!!!")],
        [gui.Text("=*"*20)],
        [gui.Text("É muito dahora isso ;-;")],
        [gui.Button('Pressione aqui')]]    #Criando conteúdo do programa, para o texto Text() e botão Button()

wind = gui.Window('Primeiro code na GUI', test)     #Criando a janela, função Window() recebe o nome da janela, e o conteúdo
wind.read()     #Depois ela precisa ser lida, usando o read() para ler o conteúdo do código
wind.close()    #Por fim close() para fechar o programa depois de rodar todo o código

'''
    Documentação = 
    https://pypi.org/project/PySimpleGUI/ -> Focado no básico
    https://pysimplegui.readthedocs.io/en/latest/ -> Documentário de verdade
'''
