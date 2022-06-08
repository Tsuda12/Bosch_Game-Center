#IMPORTS
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from random import choice
import janelas_py.JokenpoTela
import pandas as pd


#CLASSE
class Jokenpo(janelas_py.JokenpoTela.Ui_Form):
    #CONSTRUTOR
    def __init__(self):
        self.janela = uic.loadUi("janelas_ui/jokenpo.ui")
        self.janela.btn_pedra.clicked.connect(self.pedra)
        self.janela.btn_papel.clicked.connect(self.papel)
        self.janela.btn_tesoura.clicked.connect(self.tesoura)
        self.lista_palavras = ['PEDRA', 'PAPEL', 'TESOURA']
        self.janela.show()


    #MÉTODOS
    def pedra(self):
        self.janela.lbl_selecionado.setText("PEDRA")
        self.jogo()

    def papel(self):
        self.janela.lbl_selecionado.setText("PAPEL")
        self.jogo()

    def tesoura(self):
        self.janela.lbl_selecionado.setText("TESOURA")
        self.jogo()

    def jogada_pc(self):
        escolha = choice(self.lista_palavras)
        self.janela.lbl_sorteio_computador.setText(f"{escolha}")

    def jogo(self):
        self.jogada_pc()

        escolha_usuario = self.janela.lbl_selecionado.text()
        escolha_pc = self.janela.lbl_sorteio_computador.text()

        if escolha_usuario == escolha_pc:
            self.janela.lbl_sorteio_2.setText("EMPATE")

        elif escolha_usuario == "TESOURA" and escolha_pc == "PAPEL":
            self.janela.lbl_sorteio_2.setText("USUÁRIO VENCEU")
        elif escolha_usuario == "PEDRA" and escolha_pc == "TESOURA":
            self.janela.lbl_sorteio_2.setText("USUÁRIO VENCEU")
        elif escolha_usuario == "PAPEL" and escolha_pc == "PEDRA":
            self.janela.lbl_sorteio_2.setText("USUÁRIO VENCEU")

        elif escolha_pc == "TESOURA" and escolha_usuario == "PAPEL":
            self.janela.lbl_sorteio_2.setText("COMPUTADOR VENCEU")
        elif escolha_pc == "PEDRA" and escolha_usuario == "TESOURO":
            self.janela.lbl_sorteio_2.setText("COMPUTADOR VENCEU")
        elif escolha_pc == "PAPEL" and escolha_usuario == "PEDRA":
            self.janela.lbl_sorteio_2.setText("COMPUTADOR VENCEU")

