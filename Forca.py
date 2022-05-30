from PyQt5 import QtCore, QtGui, QtWidgets
import janelas.Forca_Tela


class Forca(janelas.Forca_Tela.Ui_Form):
    #CONSTRUTOR
    def __init__(self, carregar_tela=0):
        #--Carrega a tela da forca
        self.carregar_tela = uic.loadUi("janelas/forca.ui")
        self.carregar_tela.show()


