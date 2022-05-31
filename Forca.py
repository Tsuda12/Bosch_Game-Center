#BIBLIOTECAS
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from random import randint
import janelas_py.ForcaTela

#CLASSE
class Forca(janelas_py.ForcaTela.Ui_Form):
    #CONSTRUTOR
    def __init__(self, sorteio=None, palavras=[], palavra_sorteada=None, dicas=[], dica_sorteada=None):
        #--Variáveis
        self.sorteio = sorteio
        self.palavras = palavras
        self.palavra_sorteada = palavra_sorteada
        self.dicas = dicas
        self.dica_sorteada = dica_sorteada
        #--Carrega a ui da forca
        self.janela = uic.loadUi("janelas_ui/forca.ui")
        #--Chama métodos
        self.resultado_sorteio = self.sortear_numero()
        self.sortear_dica()
        self.sortear_palavra()
        self.ocultar_palavra()
        #--Exibe a janela
        self.janela.show()


    #MÉTODOS
    def sortear_palavra(self):
        self.palavras = ['CARRO', 'MACACO', 'FIFA']
        self.palavra_sorteada = self.palavras[self.resultado_sorteio]

    def sortear_dica(self):
        self.dicas = ['Meio de locomoção', 'Animal', 'Jogo eletrônico popular']
        self.dica_sorteada = self.dicas[self.resultado_sorteio]
        self.janela.lbl_txt_dica.setText(self.dica_sorteada)

    def sortear_numero(self):
        self.sorteio = randint(0, 2)
        return self.sorteio

    def ocultar_palavra(self):
        self.janela.lbl_palavra_secreta.setText('*  ' * len(self.palavra_sorteada))