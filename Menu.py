from Forca import Forca
from PyQt5 import uic, QtWidgets

class Menu():
    #Construtor
    def __init__(self, menu_principal=None, jogo_forca=None):
        #Instanciando variáveis
        self.menu_principal = menu_principal
        self.jogo_forca = jogo_forca


    #Métodos
    def iniciar(self):
        #--Chama a tela
        self.menu_principal = uic.loadUi("janelas/menu_inicial.ui")
        #--Botao forca
        self.menu_principal.botao_forca.clicked.connect(self.tela_forca)
        #--Exibe a janela
        self.menu_principal.show()

    def tela_forca(self):
        # --Chama a tela
        self.jogo_forca = uic.loadUi("janelas/jogo_forca.ui")
        # --Exibe a janela
        self.jogo_forca.show()
        #--Fecha menu principal
        self.menu_principal.close()
        #--Instancia objeto da forca
        forca = Forca()
        #--Função de sortear palavra
        forca.dica_secreta(self.jogo_forca)
