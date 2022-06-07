#IMPORTS
from PyQt5 import QtCore, QtGui, QtWidgets, uic
import janelas_py.VelhaTela


#CLASSE
class Velha(janelas_py.VelhaTela.Ui_Form):
    #CONSTRUTOR
    def __init__(self):
        self.janela = uic.loadUi("janelas_ui/velha.ui")

        self.rodada = 0

        self.janela.lbl_venceu.setHidden(True)
        self.janela.lbl_venceu_2.setHidden(True)
        self.janela.btn_1.clicked.connect(self.mudar_texto(self.janela.btn_1))
        self.janela.btn_2.clicked.connect(self.mudar_texto(self.janela.btn_2))
        self.janela.btn_3.clicked.connect(self.mudar_texto(self.janela.btn_3))
        self.janela.btn_4.clicked.connect(self.mudar_texto(self.janela.btn_4))
        self.janela.btn_5.clicked.connect(self.mudar_texto(self.janela.btn_5))
        self.janela.btn_6.clicked.connect(self.mudar_texto(self.janela.btn_6))
        self.janela.btn_7.clicked.connect(self.mudar_texto(self.janela.btn_7))
        self.janela.btn_8.clicked.connect(self.mudar_texto(self.janela.btn_8))
        self.janela.btn_9.clicked.connect(self.mudar_texto(self.janela.btn_9))

        self.janela.show()


    #MÉTODOS
    def mudar_texto(self, botao):
        if self.rodada %2 == 0:
            self.janela.label.setText("Vez do X")
            clicado = "X"
        else:
            self.janela.label.setText("Vez do O")
            clicado = "O"

        botao.setText(clicado)
        botao.setEnabled(False)

        self.rodada += 1
