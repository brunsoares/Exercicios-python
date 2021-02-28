import playsound

#Encontrando o arquivo mp3
arq = 'musica21.mp3'
music = playsound._playsoundWin(arq, True)#False faz não tocar
#_playsounwin eh para tocar musica no windows

'''
    Primeiro importamos uma biblioteca externa playsound, por ser externa necessita de uma intalação do pacote
    Apenas apertar se aparecer algum erro em "install package"
    Para o programa precisamos de uma música em mp3, disponivel na pasta do exercicio
    A variavel arq pega o diretorio da música, como está na mesma pasta apenas colocar seu nome funciona
    Já a variavel music aciona a função _playsoundWin() que como parametro tem o arq (música) e True como valor bool, false faz não tocar
    E por fim ao iniciar o programa automaticamente toca a música
'''
