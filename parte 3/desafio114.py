import requests

try:
    resposta = requests.get('http://pudim.com.br/')
except:
    print('\033[31mO site do PUDIM está off :(\033[m')
else:
    print('\033[32mO site do PUDIM está on :)\033[m')

'''
    Programa para checar se um site está online ou off
    Primeiro importamos uma biblioteca externa, request (necessita de instalação)
    Em seguida tentamos (TRY) entrar em contato com o site Pudim, pela variavel resposta
    Nessa variavel usamos o get() de request e colocamos o endereço do site
    No except, mostrará que o site do pudim está off
    Caso contrario, else, mostrará que está on
    *Pode testar desligando a internet para checar*
'''
