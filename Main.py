#BIBLIOTECAS
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from Forca import Forca
from Velha import Velha
from Jokenpo import Jokenpo
#from Velha import Velha
import janelas_py.MenuTela


#CLASSE PRINCIPAL
class Central(janelas_py.MenuTela.Ui_MainWindow):
    #CONSTRUTOR
    def __init__(self, MainWindow):
        self.setupUi(MainWindow)
        #--Botões
        self.btn_forca.clicked.connect(self.abrir_forca)
        self.btn_velha.clicked.connect(self.abrir_velha)
        self.btn_ppt.clicked.connect(self.abrir_jokenpo)

    #MÉTODOS
    def abrir_forca(self):
        self.forca = Forca()

    def abrir_velha(self):
        self.velha = Velha()

    def abrir_jokenpo(self):
        self.jokenpo = Jokenpo()


#PROGRAMA
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    central = Central(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
