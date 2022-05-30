from PyQt5 import uic
from PyQt5 import QtCore, QtGui, QtWidgets
from Forca import Forca
import janelas.Menu_Tela


class Central(janelas.Menu_Tela.Ui_MainWindow):
    #CONSTRUTOR
    def __init__(self, MainWindow, janela_forca=None):
        #--Inicializa a janela
        self.setupUi(MainWindow)
        #--Carregar tela
        self.menu = uic.loadUi("janelas/menu_inicial.ui")
        #--Botões
        self.btn_forca.clicked.connect(self.abrir_forca)
        self.btn_velha.clicked.connect(self.abrir_velha)


    #MÉTODOS
    def abrir_forca(self):
        print("ABRIU FORCA")

    def abrir_velha(self):
        print("ABRIU VELHA")


#MAIN
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    central = Central(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
