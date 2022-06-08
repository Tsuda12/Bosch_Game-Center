#IMPORTS
from PyQt5 import QtCore, QtGui, QtWidgets, uic
import janelas_py.VelhaTela


#CLASSE
class Velha(janelas_py.VelhaTela.Ui_Form):
    #CONSTRUTOR
    def __init__(self):
        self.janela = uic.loadUi("janelas_ui/velha.ui")

        self.rodada = 0

        self.janela.btn_1.clicked.connect(lambda: self.mudar_texto(self.janela.btn_1))
        self.janela.btn_2.clicked.connect(lambda: self.mudar_texto(self.janela.btn_2))
        self.janela.btn_3.clicked.connect(lambda: self.mudar_texto(self.janela.btn_3))
        self.janela.btn_4.clicked.connect(lambda: self.mudar_texto(self.janela.btn_4))
        self.janela.btn_5.clicked.connect(lambda: self.mudar_texto(self.janela.btn_5))
        self.janela.btn_6.clicked.connect(lambda: self.mudar_texto(self.janela.btn_6))
        self.janela.btn_7.clicked.connect(lambda: self.mudar_texto(self.janela.btn_7))
        self.janela.btn_8.clicked.connect(lambda: self.mudar_texto(self.janela.btn_8))
        self.janela.btn_9.clicked.connect(lambda: self.mudar_texto(self.janela.btn_9))

        self.janela.btn_enviar_2.clicked.connect(self.rejogar)

        self.janela.show()


    #MÉTODOS
    def mudar_texto(self, botao):
        if self.rodada %2 == 0:
            self.janela.label.setText("Vez do O")
            clicado = "X"
        else:
            self.janela.label.setText("Vez do X")
            clicado = "O"

        botao.setText(clicado)
        botao.setEnabled(False)

        self.rodada += 1

        self.ganhar()

    def ganhar(self):
        if self.janela.btn_1.text() != "" and self.janela.btn_1.text() == self.janela.btn_2.text() and self.janela.btn_1.text() == self.janela.btn_3.text():
            self.venceu(self.janela.btn_1, self.janela.btn_2, self.janela.btn_3)

        if self.janela.btn_4.text() != "" and self.janela.btn_4.text() == self.janela.btn_5.text() and self.janela.btn_4.text() == self.janela.btn_6.text():
            self.venceu(self.janela.btn_4, self.janela.btn_5, self.janela.btn_6)

        if self.janela.btn_7.text() != "" and self.janela.btn_7.text() == self.janela.btn_8.text() and self.janela.btn_7.text() == self.janela.btn_9.text():
            self.venceu(self.janela.btn_7, self.janela.btn_8, self.janela.btn_9)

        if self.janela.btn_1.text() != "" and self.janela.btn_1.text() == self.janela.btn_4.text() and self.janela.btn_1.text() == self.janela.btn_7.text():
            self.venceu(self.janela.btn_1, self.janela.btn_4, self.janela.btn_7)

        if self.janela.btn_2.text() != "" and self.janela.btn_2.text() == self.janela.btn_5.text() and self.janela.btn_2.text() == self.janela.btn_8.text():
            self.venceu(self.janela.btn_2, self.janela.btn_5, self.janela.btn_8)

        if self.janela.btn_3.text() != "" and self.janela.btn_3.text() == self.janela.btn_6.text() and self.janela.btn_3.text() == self.janela.btn_9.text():
            self.venceu(self.janela.btn_3, self.janela.btn_6, self.janela.btn_9)

        if self.janela.btn_1.text() != "" and self.janela.btn_1.text() == self.janela.btn_5.text() and self.janela.btn_1.text() == self.janela.btn_9.text():
            self.venceu(self.janela.btn_1, self.janela.btn_5 , self.janela.btn_9)

        if self.janela.btn_7.text() != "" and self.janela.btn_7.text() == self.janela.btn_5.text() and self.janela.btn_7.text() == self.janela.btn_3.text():
            self.venceu(self.janela.btn_7, self.janela.btn_5 , self.janela.btn_3)

    def venceu(self, btn1, btn2, btn3):
        btn1.setStyleSheet('QPushButton {background:  rgb(255, 85, 127); color: white; border:none;}')
        btn2.setStyleSheet('QPushButton {background:  rgb(255, 85, 127); color: white; border:none;}')
        btn3.setStyleSheet('QPushButton {background:  rgb(255, 85, 127); color: white; border:none;}')

        self.janela.label.setText(f"{btn1.text()} GANHOU")
        self.janela.label.setStyleSheet('QLabel {background:  rgb(255, 85, 127); color: white;}')

        self.desabilitar_botoes()

    def desabilitar_botoes(self):
        lista_botoes = [self.janela.btn_1, self.janela.btn_2, self.janela.btn_3, self.janela.btn_4, self.janela.btn_5,
            self.janela.btn_6, self.janela.btn_7, self.janela.btn_8, self.janela.btn_9]

        for botao in lista_botoes:
            botao.setEnabled(False)

    def rejogar(self):
        self.janela.close()
        self.forca = Velha()