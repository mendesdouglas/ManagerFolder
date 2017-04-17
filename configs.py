import os
#from Core.folder_view import *

LARGE_FONT = ("Verdana", 14)
NORMAL_FONT = ("Verdana", 12)
SMALL_FONT = ("Verdana", 10)



'''
DEFINIÇÕES:
PATH_SYSTEM = CAMINHO PARA ONDE ESTÁ INSTALADO O SISTEMA
PATH_TRACK = CAMINHO PARA A PASTA TRACK, ONDE AS INFORMAÇÕES DE PRODUÇÃO SERÃO GUARDADAS DENTRO DE ARQUIVOS *.JSON
PATH = CAMINHO PARA A PASTA QUE DEVE SER VERIFICADA
PATH_FILES = É A JUNÇÃO DOS CAMINHOS, DE CONFIGURAÇÃO DA PASTA ONDE FICARÁ OS JSON E O CAMINHO DA PASTA RAIZ
PATH_NETWORK = É O CAMINHO DA PASTA DE REDE
'''
#estes caminhos devem ser alterados, quando for implementado um menu e tiver a opções de escolher onde quer ser visualizado
PATH_SYSTEM = os.path.dirname(os.path.realpath(__file__))
PATH_TRACK = ("\\Tracks")
PATH_FILES = PATH_SYSTEM+PATH_TRACK
#PATH_NETWORK = DEVE SER IMPLEMENTADO
PATH = "c:\PDF Files"

print(PATH)
print(PATH_TRACK)
print(PATH_FILES)
print(PATH_SYSTEM)


