#BIBLIOTECAS
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from random import randint
from time import sleep
import janelas_py.ForcaTela


#CLASSE
class Forca(janelas_py.ForcaTela.Ui_Form):
    #CONSTRUTOR
    def __init__(self, sorteio=None, palavras=[], palavra_sorteada=None, dicas=[], dica_sorteada=None,
                 chute_certo=[], chute_errado=[], u_chute=None):
        #--Variáveis
        self.sorteio = sorteio
        self.palavras = palavras
        self.palavra_sorteada = palavra_sorteada
        self.dicas = dicas
        self.dica_sorteada = dica_sorteada
        self.chute_certo = chute_certo
        self.chute_errado = chute_errado
        self.u_chute = u_chute
        #--Carrega a ui da forca
        self.janela = uic.loadUi("janelas_ui/forca.ui")
        #--Chama métodos
        self.resultado_sorteio = self.sortear_numero()
        self.sortear_dica()
        self.sortear_palavra()
        self.ocultar_palavra()
        #--Botões
        self.janela.btn_enviar.clicked.connect(self.chute)
        self.janela.perdeu.setHidden(True)
        self.janela.ganhou.setHidden(True)
        #--Exibe a janela
        self.janela.show()


    #MÉTODOS
    def sortear_palavra(self):
        #--Cria lista de palavras e sorteia uma palavra
        self.palavras = ['CARRO', 'MACACO', 'FIFA']
        self.palavra_sorteada = self.palavras[self.resultado_sorteio]

    def sortear_dica(self):
        #--Cria uma lista de dicas e sorteia de acordo com a palavra, logo em seguida exibe na interface
        self.dicas = ['Meio de locomoção', 'Animal', 'Jogo eletrônico popular']
        self.dica_sorteada = self.dicas[self.resultado_sorteio]
        self.janela.lbl_txt_dica.setText(self.dica_sorteada)

    def sortear_numero(self):
        #--Sorteia um número para colocar na posição da lista de palavras e dicas
        self.sorteio = randint(0, 2)
        return self.sorteio

    def ocultar_palavra(self):
        #--Substitui cada caracter da palavra sorteada por *
        self.palavra_secreta = '*' * len(self.palavra_sorteada)
        self.imprimir_palavra_secreta()

    def chute(self):
        #--A letra que estiver dentro do lne_chute será o chute
        self.u_chute = self.janela.lne_chute.text().upper()
        #--Se o chute estiver dentro da palavra sorteada ela é adicionada a lista de chute certo
        if self.u_chute in self.palavra_sorteada:
            self.chute_certo.append(self.u_chute)
            #--Redefine o texto do chute para vazio
            self.janela.lne_chute.setText("")
            self.chute_correto()
            self.ganhar()
        #--Senão adiciona na lista de chutes errados
        else:
            #--Se o chute errado ainda não estiver na lista adiciona
            if self.u_chute not in self.chute_errado:
                self.chute_errado.append(self.u_chute)
            # --Redefine o texto do chute para vazio
            self.janela.lne_chute.setText("")
            #--Printa os erros no label
            for letra in self.chute_errado:
                self.janela.lbl_letras_erradas.setText(f"{self.chute_errado}")
            self.perder()

    def chute_correto(self):
        #--Lista com cada * separado
        self.palavra_secreta_list = list(self.palavra_secreta)
        #--Variável de texto vazia
        palavra_secreta_str = ""
        #Para cada *, se o chute corresponder a letra oculta, o * será igual ao chute
        for pos in range(len(self.palavra_sorteada)):
            if self.u_chute == self.palavra_sorteada[pos]:
                self.palavra_secreta_list[pos] = self.u_chute
        #Para cada posição dentro da lista, concatena dentro da variável vazia
        for pos in range(len(self.palavra_secreta_list)):
            palavra_secreta_str += self.palavra_secreta_list[pos]
        #O valor de uma variável passa para outra
        self.palavra_secreta = palavra_secreta_str
        self.imprimir_palavra_secreta()

    def imprimir_palavra_secreta(self):
        #--Variável de texto vazia
        self.palavra_secreta_escrita = ""
        #--Para cada letra dentro da palavra sorteada adiciona na variável acima e da um espaço
        for letra in self.palavra_secreta:
            self.palavra_secreta_escrita += letra.upper() + '  '
        self.janela.lbl_palavra_secreta.setText(self.palavra_secreta_escrita)

    def perder(self):
        if len(self.chute_errado) == 7:
            self.janela.perdeu.setHidden(False)
            sleep(2)
            self.janela.btn_enviar.setHidden(True)
            self.janela.lne_chute.setHidden(True)

    def ganhar(self):
        if self.palavra_secreta == self.palavra_sorteada:
            self.janela.ganhou.setHidden(False)
            sleep(2)
            self.janela.btn_enviar.setHidden(True)
            self.janela.lne_chute.setHidden(True)


